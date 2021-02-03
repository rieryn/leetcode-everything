  using System;

public static int HighestProductOf3(int[] arrayOfInts)
{
    if (arrayOfInts.Length < 3)
    {
        throw new ArgumentException("Less than 3 elements");
    }

    int highest = Math.Max(arrayOfInts[0], arrayOfInts[1]);
    int lowest = Math.Min(arrayOfInts[0], arrayOfInts[1]);

    int highestProductOf2 = arrayOfInts[0] * arrayOfInts[1];
    int lowestProductOf2 = arrayOfInts[0] * arrayOfInts[1];
    int highestProductOf3 = arrayOfInts[0] * arrayOfInts[1] * arrayOfInts[2];

    // Walk through items, starting at index 2
    for (int i = 2; i < arrayOfInts.Length; i++)
    {
        int current = arrayOfInts[i];

        // Do we have a new highest product of 3?
        // It's either the current highest,
        // or the current times the highest product of two
        // or the current times the lowest product of two
        highestProductOf3 = Math.Max(Math.Max(
            highestProductOf3,
            current * highestProductOf2),
            current * lowestProductOf2);

        highestProductOf2 = Math.Max(Math.Max(
            highestProductOf2,
            current * highest),
            current * lowest);

        lowestProductOf2 = Math.Min(Math.Min(
            lowestProductOf2,
            current * highest),
            current * lowest);

        highest = Math.Max(highest, current);
        lowest = Math.Min(lowest, current);
    }

    return highestProductOf3;
}