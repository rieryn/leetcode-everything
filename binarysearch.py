search = [1,2,3,4,5,6]

def bSearch(target, search):
  left = 0
  right = len(search)-1
  while(left <= right):
    mid = int((left+right)/2)
    if(search[mid] == target):
      print(left)
      return mid
    if(search[mid]< target):
      left = mid +1
    if(search[mid]> target):
      right = mid
  return 0
print(bSearch(6, search))