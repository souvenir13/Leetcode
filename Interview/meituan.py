# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 18:29:18 2017

@author: bowen
"""

def method(l,k):
    n = len(l)
    ans = 0
    for i in range(n):
        for j in range(i,n):
            s = sum(l[i:j+1])
            if s%k == 0 :
                ans = max(ans,j+1-i)
    return ans

class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild
        
class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        if self.root.elem == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  # 此结点的子树还没有齐。
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃。
                
    def leave(self,root):   #递归求叶子节点个数
        if root==None:
            return 0
        elif root.lchild ==None and root.rchild == None :
            return 1
        else:
            return (self.leave(root.lchild)+self.leave(root.rchild))
        
    def sonOfson(self,root):
        if root==None:
            return 0
        elif root.lchild==None and 

if __name__ == '__main__':
    """主函数"""
#    elems = range(10)           #生成十个数据作为树节点
    num_list = input().strip().split()
    m = int(num_list[0])
    n = int(num_list[1])
    
    tree = Tree()          #新建一个树对象
    for i in range(m):
        mem_list = input().strip().split()
        for j in range(len(mem_list)):
            if mem_list[j] == '*' :
                tree.add(None)
            tree.add(mem_list[j])  #逐个添加树的节点
    
    print ('\n叶子节点个数:')
    num = tree.leave(tree.root)
    print (num)
#def method2(n,m):
#    root_list = input().strip().split()
#    rootNode = root_list[0]
#    
#    for i in range(n):
#        tuijian_list = input()
#        

ans1 = method([1,2,3,4,5],5)
print (ans1)
    