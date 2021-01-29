  public static void Reverse(char[] arrayOfChars)
{
    int leftIndex = 0;
    int rightIndex = arrayOfChars.Length - 1;

    while (leftIndex < rightIndex)
    {
        // Swap characters
        char temp = arrayOfChars[leftIndex];
        arrayOfChars[leftIndex] = arrayOfChars[rightIndex];
        arrayOfChars[rightIndex] = temp;

        // Move towards middle
        leftIndex++;
        rightIndex--;
    }
}