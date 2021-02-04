  LinkedListNode * reverse(LinkedListNode* headOfList)
{
    LinkedListNode* currentNode = headOfList;
    LinkedListNode* previousNode = nullptr;
    LinkedListNode* nextNode = nullptr;

    // until we have 'fallen off' the end of the list
    while (currentNode) {

        // copy a pointer to the next element
        // before we overwrite currentNode.next
        nextNode = currentNode->next_;

        // reverse the 'next' pointer
        currentNode->next_ = previousNode;

        // step forward in the list
        previousNode = currentNode;
        currentNode = nextNode;
    }

    return previousNode;
}