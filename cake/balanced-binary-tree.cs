  using System;
using System.Collections.Generic;

public class NodeDepthPair
{
    public BinaryTreeNode Node { get; }

    public int Depth { get; }

    public NodeDepthPair(BinaryTreeNode node, int depth)
    {
        Node = node;
        Depth = depth;
    }
}

public static bool IsBalanced(BinaryTreeNode treeRoot)
{

    // a tree with no nodes is superbalanced, since there are no leaves!
    if (treeRoot == null) {
        return true;
    }

    var depths = new List<int>(3);  // We short-circuit as soon as we find more than 2

    // Nodes will store pairs of a node and the node's depth
    var nodes = new Stack<NodeDepthPair>();
    nodes.Push(new NodeDepthPair(treeRoot, 0));

    while (nodes.Count > 0)
    {
        // Pop a node and its depth from the top of our stack
        var nodeDepthPair = nodes.Pop();
        var node = nodeDepthPair.Node;
        var depth = nodeDepthPair.Depth;

        if (node.Left == null && node.Right == null)
        {
            // Case: we found a leaf

            // We only care if it's a new depth
            if (!depths.Contains(depth))
            {
                depths.Add(depth);

                // Two ways we might now have an unbalanced tree:
                //   1) more than 2 different leaf depths
                //   2) 2 leaf depths that are more than 1 apart
                if (depths.Count > 2
                    || (depths.Count == 2 && Math.Abs(depths[0] - depths[1]) > 1))
                {
                    return false;
                }
            }
        }
        else
        {
            // Case: this isn't a leaf - keep stepping down

            if (node.Left != null)
            {
                nodes.Push(new NodeDepthPair(node.Left, depth + 1));
            }

            if (node.Right != null)
            {
                nodes.Push(new NodeDepthPair(node.Right, depth + 1));
            }
        }
    }

    return true;
}