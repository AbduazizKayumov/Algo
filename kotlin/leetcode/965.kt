package leetcode

/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun isUnivalTree(root: TreeNode?, value: Int = -1): Boolean {
        if (root == null)
            return true

        var check = value
        if (check == -1)
            check = root.`val`

        if (root.`val` != check)
            return false

        return isUnivalTree(root.left, check) && isUnivalTree(root.right, check)
    }
}