  int f(const vector<int>& stockPrices)
{
    if (stockPrices.size() < 2) {
        throw invalid_argument("Getting a profit requires at least 2 prices");
    }

    int mprice = stockPrices[0];
    int maxp = stockPrices[1] - stockPrices[0];

    for (int i = 1; i < stockPrices.size(); i++) {

        maxp = max(maxp, stockPrices[i]- mprice);
        mprice = min(mprice, stockPrices[i]);
    }

    return maxp;
}