# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:29:14 2017

@author: bowen

keyword: 数据结构、树、链表、数组、堆、递归
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class TreeLinkNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None
        self.parent = None
        
class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        '''
        由先序遍历序列和中序遍历序列构建二叉树
        '''
        if len(preorder)==0:
            return None;
            
        rootVal = preorder[0]
        root = TreeNode(rootVal)

        for i in range(len(inorder)):
            if inorder[i] == rootVal:
                break

        root.left = self.buildTree(preorder[1:1+i],inorder[:i])
        root.right = self.buildTree(preorder[1+i:],inorder[i+1:])
        
        return root
    
    def levelTraversal(self,root):
        '''
        层次遍历(利用队列)
        '''
        if root==None:
            return None
        myQueue = []
        myQueue.append(root)
        while myQueue:
            node = myQueue.pop(0)
            print (node.val)
            if node.left!=None:
                myQueue.append(node.left)
            if node.right!=None:
                myQueue.append(node.right)
        
    def deepTraversal(self,root):
        '''
        深度遍历(利用递归)
        '''
        if root==None:
            return None
        print (root.val)
        self.deepTraversal(root.left)
        self.deepTraversal(root.right)
        
    def middleTraversal(self,root):
        '''
        中序遍历
        (与用递归的方法实现先序遍历、后序遍历类似，仅改变print语句顺序即可)
        '''
        if root==None:
            return None
        self.middleTraversal(root.left)
        print (root.val)
        self.middleTraversal(root.right)
        
    def middleStack(self,root):
        '''
        用栈实现中序遍历
        '''
        if root == None:
            return None
        myStack = []
        node = root
        while node or myStack:
            while node != None:
                myStack.append(node)
                node = node.left
            node = myStack.pop()
            print (node.val)
            node = node.right
    
    def frontStack(self,root):
        if root == None:
            return None
        myStack = []
        node = root
        while node or myStack:
            while node:
                print (node.val)
                myStack.append(node)
                node = node.left
            node = myStack.pop()
            node = node.right
            
    def behindStack(self,root):
        '''
        用栈实现后序遍历(***)
        '''
        if root == None:
            return None
        myStack1 = []
        myStack2 = []
        myStack1.append(root)
        while myStack1:
            #这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            myStack2.append(node)
            if node.left:
                myStack1.append(node.left)
            if node.right:
                myStack1.append(node.right)
            
        while myStack2:
            #将myStack2中的元素出栈，即为后序遍历次序
            print (myStack2.pop().val)
    
    def GetNext(self,pNode):
        '''
        二叉树中序遍历的下一个结点
        '''
        if pNode == None:
            return None
        if pNode.right:
            node = pNode.right
            while node.left:
                node = node.left
            return node
        elif pNode.parent:
            if pNode == pNode.parent.left:
                return pNode.parent
            if pNode == pNode.parent.right:
                node = pNode.parent
                while (node and node.parent):
                    if node == node.parent.left:
                        return node.parent
                    node = node.parent
        else:
            return None
    
"""
二叉树中和为某一值路径
"""

if __name__ == '__main__':  
    pre_order = [1, 2, 4, 7, 3, 5, 6, 8]  
    mid_order = [4, 7, 2, 1, 5, 3, 8, 6] 
    root = Solution().buildTree(pre_order,mid_order)
#    Solution().levelTraversal(root)
#    Solution().deepTraversal(root)
#    Solution().middleTraversal(root)
#    Solution().middleStack(root)
#    Solution().frontStack(root)
    Solution().behindStack(root)