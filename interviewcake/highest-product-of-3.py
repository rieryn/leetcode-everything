def f(nums):
	h_num = 1
	neg_num = 0
	h_prod2 = 1
	h_prod3 = 1
	for i in nums:
		print(h_prod3)
		if h_prod2*i > h_prod3:
			h_prod3 = h_prod2*i
		if i<0:
			if neg_num*i *h_num > h_prod3:
				h_prod3 = neg_num*i *h_num
			if neg_num*i > h_prod2:
				h_prod2 = neg_num*i
			if i< neg_num:
				neg_num = i
		if i*h_num >h_prod2:
		    h_prod2 = i*h_num
		if i > h_num:
			h_num = i
	return h_prod3