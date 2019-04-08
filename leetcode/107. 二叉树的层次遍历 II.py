# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if root is None:
            return []
        lever = [root]
        ret = []
        while len(lever) > 0:
            tmp = []
            lever_val = []
            for n in lever:
                lever_val.append(n.val)
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            lever = tmp
            ret.insert(0, lever_val)
        return ret


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(29)
    root.right = TreeNode(80)
    print(Solution().levelOrderBottom(root))
