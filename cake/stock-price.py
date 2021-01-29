def f(stocks):
	lp = stocks[0]
	m = 0
	for i in stocks:
		m = max(i-lp, m)
		lp = min(i, lp)
	return m