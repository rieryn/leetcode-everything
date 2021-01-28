public static bool IsFirstComeFirstServed(int[] takeOutOrders, int[] dineInOrders, int[] servedOrders)
{
    int takeOutOrdersIndex = 0;
    int dineInOrdersIndex = 0;

    foreach (var order in servedOrders)
    {
        if (takeOutOrdersIndex < takeOutOrders.Length && order == takeOutOrders[takeOutOrdersIndex])
        {
            takeOutOrdersIndex++;
        }
        else if (dineInOrdersIndex < dineInOrders.Length && order == dineInOrders[dineInOrdersIndex])
        {
            dineInOrdersIndex++;
        }
        else
        {
            return false;
        }
    }

    if (dineInOrdersIndex != dineInOrders.Length || takeOutOrdersIndex != takeOutOrders.Length) {
        return false;
    }

    return true;
}