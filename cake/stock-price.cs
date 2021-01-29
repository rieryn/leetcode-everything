using System;

public static int Getmp(int[] stocks)
{
    if (stocks.Length < 2)
    {
        throw new ArgumentException("stocks <2",
            nameof(stocks));
    }
    int minPrice  = stocks[0];
    int mp = stocks[1] - stocks[0];

    for (int i = 1; i < stocks.Length; i++)
    {
        mp = Math.Max(mp, stocks[i] - minPrice);
        minPrice = Math.Min(minPrice, stocks[i]);
    }

    return mp;
}