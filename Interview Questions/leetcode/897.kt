package leetcode

fun increasingBST(root: TreeNode?): TreeNode? {
    if (root == null) return null
    return swap(root, null)
}

fun swap(root: TreeNode?, node: TreeNode?): TreeNode? {
    if (root == null) return node

    val right = swap(root.right, node)
    root.right = right

    val left = swap(root.left, root)
    root.left = null
    return left
}