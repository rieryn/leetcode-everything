
def f(nums):
	if len(nums)<=1:
		print("error")
	prod = 1
	f = []
	for i in range(len(nums)):
		f.append(prod)
		prod = prod*nums[i]
		#last element can be, should be skipped
	prod = 1
	for i in range(len(nums)-1, -1, -1):
		f[i] = f[i]*prod
		prod = prod*nums[i]

	return f