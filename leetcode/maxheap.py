maxheap = []

def insert(maxheap, val):
  maxheap.append(val)
  float(maxheap)

def peek(maxheap):
  return maxheap[0]

def pop(maxheap):
  max = maxheap[0]
  end = len(maxheap)-1
  maxheap[0] = maxheap[end]
  maxheap.pop(end)
  print(maxheap)
  sink(maxheap)
  return max
  
def float(maxheap):
  i = len(maxheap)-1
  while i>0 and maxheap[i]>maxheap[(i-1)//2]:
    maxheap[i], maxheap[(i-1)//2] = maxheap[(i-1)//2],maxheap[i]
    i = (i-1)//2

def sink(maxheap):
  i = 0
  while (i+1)*2<len(maxheap) and maxheap[i]<max(maxheap[(i+1)*2],maxheap[(i+1)*2-1]):
    if maxheap[(i+1)*2]<maxheap[(i+1)*2-1]:
      maxheap[i], maxheap[(i+1)*2-1] = maxheap[(i+1)*2-1],maxheap[i]
    else:
      maxheap[i], maxheap[(i+1)*2] = maxheap[(i+1)*2],maxheap[i]
    i = (i+1)*2