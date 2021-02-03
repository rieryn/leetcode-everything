  size_t changePossibilitiesBottomUp(int amount, const vector<int>& denominations)
{
    vector<size_t> waysOfDoingNCents(amount + 1);  // vector of zeros from 0..amount
    waysOfDoingNCents[0] = 1;

    for (const int coin : denominations) {
        for (int higherAmount = coin; higherAmount <= amount; ++higherAmount) {
            int higherAmountRemainder = higherAmount - coin;
            waysOfDoingNCents[higherAmount] += waysOfDoingNCents[higherAmountRemainder];
        }
    }

    return waysOfDoingNCents[amount];
}