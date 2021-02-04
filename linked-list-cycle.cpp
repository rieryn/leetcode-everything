  bool containsCycle(const LinkedListNode* firstNode)
{
    // start both runners at the beginning
    const LinkedListNode* slowRunner = firstNode;
    const LinkedListNode* fastRunner = firstNode;

    // until we hit the end of the list
    while (fastRunner != nullptr && fastRunner->next_) {
        slowRunner = slowRunner->next_;
        fastRunner = fastRunner->next_->next_;

        // case: fastRunner is about to "lap" slowRunner
        if (fastRunner == slowRunner) {
            return true;
        }
    }

    // case: fastRunner hit the end of the list
    return false;
}