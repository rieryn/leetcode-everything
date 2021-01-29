  public static int ChangePossibilitiesBottomUp(int amount, int[] denominations)
{
    // Array of zeros from 0..amount
    int[] waysOfDoingNCents = new int[amount + 1];

    waysOfDoingNCents[0] = 1;

    foreach (int coin in denominations)
    {
        for (int higherAmount = coin; higherAmount <= amount; higherAmount++)
        {
            int higherAmountRemainder = higherAmount - coin;
            waysOfDoingNCents[higherAmount] +=
                waysOfDoingNCents[higherAmountRemainder];
        }
    }

    return waysOfDoingNCents[amount];
}