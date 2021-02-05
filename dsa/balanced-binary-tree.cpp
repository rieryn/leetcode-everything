bool isBalanced(const BinaryTreeNode* treeRoot)
{

    // a tree with no nodes is superbalanced, since there are no leaves!
    if (treeRoot == nullptr) {
        return true;
    }

    // will have up to 3 elements
    size_t depths[3];
    size_t depthCount = 0;

    // nodes will store pairs of a node and the node's depth
    stack<pair<const BinaryTreeNode*, size_t>> nodes;
    nodes.push(make_pair(treeRoot, 0));

    while (!nodes.empty()) {

        // get a node and its depth from the top of stack and pop it
        const BinaryTreeNode* node = nodes.top().first;
        size_t depth = nodes.top().second;
        nodes.pop();

        // case: we found a leaf
        if (!node->left_ && !node->right_) {

            // we only care if it's a new depth
            if (depthCount == 0 ||
                find(depths, depths + depthCount, depth) == depths + depthCount) {
                depths[depthCount] = depth;
                ++depthCount;

                // two ways we might now have an unbalanced tree:
                //   1) more than 2 different leaf depths
                //   2) 2 leaf depths that are more than 1 apart
                if (depthCount > 2 ||
                        (depthCount == 2 &&
                        max(depths[0], depths[1]) - min(depths[0], depths[1]) > 1)) {
                    return false;
                }
            }
        }

        // case: this isn't a leaf - keep stepping down
        else {
            if (node->left_) {
                nodes.push(make_pair(node->left_, depth + 1));
            }
            if (node->right_) {
                nodes.push(make_pair(node->right_, depth + 1));
            }
        }
    }

    return true;
}