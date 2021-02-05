// Raycast Engine Code
// =====================
// Inspired by/modified from:
// https://github.com/hunterloftis/playfuljs/blob/master/content/demos/raycaster.html
// Notes:
// Improved Raycasting algorithm.
// - The raycast uses a stack instead of recursion.
//   This lowers function call overhead (the bane of games),
//   and it also lowers the amount of objects created
//   (the other bane of games).
// - NOTE: Runs a heck of a lot better in node-webkit
// =====================

var CIRCLE = Math.PI * 2;

// Texture
// =========
// TODO: switch to the ability to use atlases
function Texture(options){
  this.width = 0;
  this.height = 0;
  this.img = undefined;
  
  if (options){
    for (var prop in options)
      if (this.hasOwnProperty(prop))
        this[prop] = options[prop];
    
    if(options.hasOwnProperty('src')){
      this.img = new Image();
      this.img.src = options.src;
    }
  }
}

// The Map
// =======================
function RayMap(options){
  this.walls = [];
  this.floor = [];
  this.ceiling = [];
  this.skyBox = undefined;
  this.light = 1;
  this.width = 0;
  this.height = 0;
  this.outdoors = false;
  this.wallTextures = [];
  this.floorTextures = [];
  this.ceilingTextures = [];
  
  if (options){
    for (var prop in options)
      if (this.hasOwnProperty(prop))
        this[prop] = options[prop];
  }
}

RayMap.prototype = {
  Get: function(x, y){
    x = x | 0;
    y = y | 0;
    if(x < 0 || x >= this.width || y < 0 || y >= this.height) return -1;
    return this.walls[y * this.width + x];
  },
  
  Raycast: function(point, angle, range, fullRange, layer){
    if(fullRange === undefined)
      fullRange = false;
    if(!layer)
        layer = 'walls';
    var cells = [];
    var sin = Math.sin(angle);
    var cos = Math.cos(angle);
    
    var stepX, stepY, nextStep;
    nextStep = { x: point.x, y: point.y, cell: 0, distance: 0 };
    do{
      cells.push(nextStep);
      if (!fullRange && nextStep.cell > 0)
        break;
      stepX = this.__step(sin, cos, nextStep.x, nextStep.y);
      stepY = this.__step(cos, sin, nextStep.y, nextStep.x, true);
      nextStep = stepX.length2 < stepY.length2
        ? this.__inspect(stepX, 1, 0, nextStep.distance, stepX.y, cos, sin, layer)
        : this.__inspect(stepY, 0, 1, nextStep.distance, stepY.x, cos, sin, layer);
    } while (nextStep.distance <= range);
    
    return cells;
  },
  
  __step: function(rise, run, x, y, inverted){
    if (run === 0) return { length2: Infinity };
    var dx = run > 0 ? Math.floor(x + 1) - x : Math.ceil(x - 1) - x;
    var dy = dx * rise / run;
    return {
      x: inverted ? y + dy : x + dx,
      y: inverted ? x + dx : y + dy,
      length2: dx * dx + dy * dy
    };
  },
  
  __inspect: function(step, shiftX, shiftY, distance, offset, cos, sin, layer){
    var dx = cos < 0 ? shiftX : 0;
    var dy = sin < 0 ? shiftY : 0;
    var index = (((step.y - dy) | 0) * this.width) + ((step.x - dx) | 0);
    step.cell = (index < 0 || index >= this[layer].length) ? -1 : this[layer][index];
    step.distance = distance + Math.sqrt(step.length2);
    
    if(this.outdoors){
      if (shiftX) step.shading = cos < 0 ? 2 : 0;
      else step.shading = sin < 0 ? 2 : 1;
    }
    else step.shading = 0;
    step.offset = offset - (offset | 0);
    return step;
  }
};

// The Camera
// ==========================
function RayCamera(options){
  this.fov = Math.PI * 0.4;
  this.range = 14;
  this.lightRange = 5;
  this.position = { x: 0, y: 0 };
  this.direction = Math.PI * 0.5;
  
  if (options){
    for (var prop in options)
      if (this.hasOwnProperty(prop))
        this[prop] = options[prop];
  }
  
  this.spacing = this.width / this.resolution;
}

RayCamera.prototype = {
  Rotate: function(angle){
    this.direction = (this.direction + angle + CIRCLE) % (CIRCLE);
  }
};

// The Render Engine
// ==============================
function RaycastRenderer(options){
  this.width = 640;
  this.height = 360;
  this.resolution = 320;
  this.textureSmoothing = false;
  this.domElement = document.createElement('canvas');
  
  if (options){
    for (var prop in options)
      if (this.hasOwnProperty(prop))
        this[prop] = options[prop];
  }
  
  this.domElement.width = this.width;
  this.domElement.height = this.height;
  this.ctx = this.domElement.getContext('2d');
  this.spacing = this.width / this.resolution;
}

RaycastRenderer.prototype = {
  __project: function(height, angle, distance){
    var z = distance * Math.cos(angle);
    var wallHeight = this.height * height / z;
    var bottom = this.height / 2 * (1 + 1/z);
    return {
      top: bottom - wallHeight,
      height: wallHeight
    };
  },
  
  __drawSky: function(camera, map){
    if(map.skybox && map.skybox.img){
      var width = this.width * (CIRCLE / camera.fov);
      var left = -width * camera.direction / CIRCLE;
      
      this.ctx.save();
      this.ctx.drawImage(map.skybox.img, left, 0, width, this.height);
      
      if (left < width - this.width)
        this.ctx.drawImage(map.skybox.img, left + width, 0, width, this.height);
      
      if (map.light > 0){
        this.ctx.fillStyle = '#ffffff';
        this.ctx.globalAlpha = map.light * 0.1;
        this.ctx.fillRect(0, this.height * 0.5, this.width, this.height * 0.5);
      }
      
      this.ctx.restore();
    }
  },
  
  __drawColumn: function(column, ray, angle, camera, textures){
    var left = Math.floor(column * this.spacing);
    var width = Math.ceil(this.spacing);
    var hit = -1;
    
    while(++hit < ray.length && ray[hit].cell <= 0);
    
    var texture;
    var textureX = 0;
    if(hit < ray.length){
      // TODO: Deal with transparent walls here somehow
      var step = ray[hit];
      texture = textures[step.cell > textures.length ? 0 : step.cell - 1];
      textureX = (texture.width * step.offset) | 0;
      var wall = this.__project(1, angle, step.distance);
      
      this.ctx.globalAlpha = 1;
      this.ctx.drawImage(texture.img, textureX, 0, 1, texture.height, left, wall.top, width, wall.height);
      
      this.ctx.fillStyle = '#000000';
      this.ctx.globalAlpha = Math.max((step.distance + step.shading) / camera.lightRange, 0);
      this.textureSmoothing ?
          this.ctx.fillRect(left, wall.top, width, wall.height)
        : this.ctx.fillRect(left | 0, wall.top | 0, width, wall.height + 1);
    }
  },
  
  __drawColumns: function(camera, map){
    this.ctx.save();
    this.ctx.imageSmoothingEnabled = this.textureSmoothing;
    for(var col = 0; col < this.resolution; col++){
      var angle = camera.fov * (col / this.resolution - 0.5);
      var ray = map.Raycast(camera.position, camera.direction + angle, camera.range);
      this.__drawColumn(col, ray, angle, camera, map.wallTextures);
    }
    this.ctx.restore();
  },
  
  Render: function(camera, map){
      this.__drawSky(camera, map);
      if (map.wallTextures.length > 0)
        this.__drawColumns(camera, map);
  },
  
  Raycast: function(point, angle, range){
    if (this.map)
      return this.map.Raycast(point, angle, range);
    return [];
  }
};

// Raycast Demo code
// ==================
// Controls and player object modified from same thing
// as the Raycast Engine
// ======================
var canvas = document.getElementById('canv');
var ctx = canvas.getContext('2d');

var wallTex = new Texture({
  src: 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAt0lEQVRYR+2XMQ7DIAxF7Qv0Ol1g416Ie7HBkuvkAk0+rZEitc3kKMO3FDlCiP/9kACriLz2b0RrzX5dc4xxrq8wAGEMIocQpPfumlV1aEFzGNhDbBAGvANapkkDJEACJEACJEACbwLLQ/S5zvfAJdfxR/OwBTByRaBYvgdIgATuSwDngHdzgobkK4Gcs6SU3M+iUwO11mHEK/80gNJBwTtKKcctsEbRhGECk7yydeKzOfWu+N/6G9zvvhAOHLZZAAAAAElFTkSuQmCC',
  width: 32,
  height: 32
});
function MiniMap(options){
  this.target = undefined;
  this.width = 22;
  this.height = 22;
  this.cellSize = 4;
  
  if (options){
    for(var prop in options)
      if (this.hasOwnProperty(prop))
        this[prop] = options[prop];
  }
  
  if(this.target === undefined)
    this.target = document.createElement('canvas');
  this.target.width = this.width * this.cellSize;
  this.target.height = this.height * this.cellSize;
  this.ctx = this.target.getContext('2d');
}

MiniMap.prototype = {
  LoadMap: function(map){
    if(this.width != map.width){
      this.width = map.width;
      this.target.width = this.width * this.cellSize;
    }
    if(this.height != map.height){
      this.height = map.height;
      this.target.height = this.height * this.cellSize;
    }
    
    this.ctx.fillStyle = '#00ffff';
    for(var y = 0; y < this.height; y++){
      for(var x = 0; x < this.width; x++){
        if(map.walls[(this.height - y - 1)*map.width + (this.width - x - 1)] === 0)
          this.ctx.fillRect(x * this.cellSize, y * this.cellSize, this.cellSize, this.cellSize);
      }
    }
  },
  
  RenderRelPlayer: function(ctx, playerPos){
    var pX = (this.width - (playerPos.x | 0) - 1) * this.cellSize;
    var pY = (this.height - (playerPos.y | 0) - 1) * this.cellSize;
    ctx.drawImage(this.target, -pX, -pY, this.target.width, this.target.height);
    ctx.fillStyle = '#ff0000';
    ctx.fillRect(0, 0, this.cellSize, this.cellSize);
  },
  
  RenderRelMap: function(ctx, pos, playerPos){
    var pX = (this.width - (playerPos.x | 0) - 1) * this.cellSize;
    var pY = (this.height - (playerPos.y | 0) - 1) * this.cellSize;
    ctx.drawImage(this.target, pos.x, pos.y, this.target.width, this.target.height);
    ctx.fillStyle = '#ff0000';
    ctx.fillRect(pos.x + pX, pos.y + pY, this.cellSize, this.cellSize);
  }
};

var miniMap = new MiniMap();

var map = new RayMap({
  width: 22,
  height: 22,
  light: 2,
  walls: [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,
          1,1,1,0,0,0,1,0,1,1,0,1,1,0,0,0,0,0,1,1,1,1,
          1,1,1,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,1,1,1,1,
          1,1,1,0,0,0,1,1,0,1,0,1,1,0,0,0,0,0,0,0,1,1,
          1,1,1,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,
          1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,
          1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,0,1,0,1,1,
          1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,0,0,0,1,0,1,1,
          1,1,1,1,0,1,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,1,
          1,1,1,1,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,1,1,
          1,1,1,1,1,1,0,1,1,0,0,0,0,1,0,1,0,1,0,1,1,1,
          1,1,1,1,0,0,0,1,1,1,0,0,1,1,0,1,0,0,0,1,1,1,
          1,1,1,1,0,0,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,
          1,1,1,1,0,0,1,1,1,1,0,1,0,0,0,1,0,1,1,1,1,1,
          1,1,1,1,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,0,0,1,
          1,1,1,1,1,0,1,1,1,0,1,1,0,0,0,0,0,1,0,1,0,1,
          1,1,1,1,0,0,1,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1,
          1,1,1,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,0,0,1,
          1,1,1,1,0,0,1,0,1,0,0,1,1,1,1,1,0,1,0,1,0,1,
          1,1,1,1,1,0,0,0,1,0,0,1,1,1,1,1,0,0,0,0,0,1,
          1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  wallTextures: [wallTex]
});

miniMap.LoadMap(map);

var camera = new RayCamera();

var renderer = new RaycastRenderer({
  width: 640,
  height: 360,
  textureSmoothing: false,
  domElement: canvas
});

function Controls() {
  this.codes  = { 37: 'left', 39: 'right', 38: 'forward', 40: 'backward' };
  this.states = { 'left': false, 'right': false, 'forward': false, 'backward': false };
  document.addEventListener('keydown', this.onKey.bind(this, true), false);
  document.addEventListener('keyup', this.onKey.bind(this, false), false);
}

Controls.prototype.onKey = function(val, e) {
  var state = this.codes[e.keyCode];
  if (typeof state === 'undefined') return;
  this.states[state] = val;
  e.preventDefault && e.preventDefault();
  e.stopPropagation && e.stopPropagation();
};

var controls = new Controls();

var player = {
  position: {x: 4.5, y: 2.5},
  direction: Math.PI * 0.3,
  rotate: function(angle) {
    this.direction = (this.direction + angle + CIRCLE) % (CIRCLE);
    camera.direction = this.direction;
  },
  walk: function(distance, map){
    var dx = Math.cos(this.direction) * distance;
    var dy = Math.sin(this.direction) * distance;
    if (map.Get(this.position.x + dx, this.position.y) <= 0) this.position.x += dx;
    if (map.Get(this.position.x, this.position.y + dy) <= 0) this.position.y += dy;
    camera.position.x = this.position.x;
    camera.position.y = this.position.y;
  },
  update: function(controls, map, seconds){
    if (controls.left) this.rotate(-Math.PI * seconds);
    if (controls.right) this.rotate(Math.PI * seconds);
    if (controls.forward) this.walk(3 * seconds, map);
    if (controls.backward) this.walk(-3 * seconds, map);
  }
};

camera.direction = player.direction;
camera.position.x = player.position.x;
camera.position.y = player.position.y;

var stats = new Stats();
stats.setMode(0);
stats.domElement.style.position = 'absolute';
stats.domElement.style.left = '0px';
stats.domElement.style.top = '0px';
document.body.appendChild(stats.domElement);

var lastTime = 0;
var mapPos = {x: -44, y: -44};
function UpdateRender(time) {
  stats.begin();
  var seconds = (time - lastTime) / 1000;
  lastTime = time;
  if (seconds < 0.2) {
    player.update(controls.states, map, seconds);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    renderer.Render(camera, map);
    ctx.save();
    ctx.translate(50, 100);
    ctx.rotate(-(player.direction - Math.PI * 0.5));
    miniMap.RenderRelMap(ctx, mapPos, player.position);
    ctx.restore();
  }
  requestAnimationFrame(UpdateRender);
  stats.end();
}

requestAnimationFrame(UpdateRender);