/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
    public class Solution
    {
        private bool Helper(TreeNode node, int? min = null, int? max = null)
        {
            if (node == null)
            {
                return true;
            }

            if ((min.HasValue && node.val <= min) || (max.HasValue && node.val >= max))
            {
                return false;
            }

            
            return Helper(node.left, min, node.val) && Helper(node.right, node.val, max);
        }

        public bool IsValidBST(TreeNode node) => Helper(node);
    }