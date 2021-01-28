  bool isFirstComeFirstServed(const vector<int>& takeOutOrders,
                            const vector<int>& dineInOrders,
                            const vector<int>& servedOrders)
{
    auto takeOutOrdersIter = takeOutOrders.cbegin();
    auto dineInOrdersIter = dineInOrders.cbegin();

    for (int order : servedOrders) {
        if (takeOutOrdersIter != takeOutOrders.cend() && order == *takeOutOrdersIter) {
            ++takeOutOrdersIter;
        }

        else if (dineInOrdersIter != dineInOrders.cend() && order == *dineInOrdersIter) {
            ++dineInOrdersIter;
        }

        else {
            return false;
        }
    }

    if (dineInOrdersIter != dineInOrders.cend() || takeOutOrdersIter != takeOutOrders.cend()) {
        return false;
    }

    return true;
}