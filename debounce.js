//debounce waits for timer end and no new invocations
function debounce(callback, wait){
	let timeout
	return function(...args){
	clearTimeout(timeout)
	timeout = setTimeout(()=>callback.apply(this,args),wait)
	}
}

function bark(){
	console.log('says', this.name)
}

const doggo = {
	name: 'rrrofer',
	speak: debounce(bark)
}

doggo.speak()
doggo.speak()
doggo.speak()

