## To use:
## Must set root = None after implementation of AVLTree
## Insert next root like example :
##  root = Tree.insert(root, 1)

class TreeNode:
    
    def __init__(self,key):
        self.key = key
        self.leftChild = None
        self.rightChild = None
        self.height = 1

class AVLTree:

    ## argument takes the tree , a parent placeholder , and the key to insert
    ## with the node
    def insert(self,parent,key):

    ## if no parent node, create one
        if parent is None:
            return TreeNode(key)

    ## if the value to be inserted is less than the parent key
        ## insert it from the parent's left side 
        elif key < parent.key:
            parent.leftChild = self.insert(parent.leftChild, key)
        else:
        ## otherwise insert it to the parent;s right side
            parent.rightChild = self.insert(parent.rightChild, key)

        ## recalculate the new height of the tree
        ## later used to correct tree order
        parent.height = 1 + max(self.getHeight(parent.leftChild),self.getHeight(parent.rightChild))

        ## call the balance function
        ## used to choose which rotation strategy to use 
        balance = self.Balance(parent)

        ## rotate right
        if balance > 1 and key < parent.leftChild.key:
            return self.rotateRight(parent)

        ## rotate left 
        if balance < -1 and key > parent.rightChild.key:
            return self.rotateLeft(parent)

        ## rotate right, then left 
        if balance < -1 and key < parent.rightChild.key:
            parent.rightChild = self.rotateRight(parent.rightChild)
            return self.rotateLeft(self.key)

        ## rotate left, then right 
        if balance > 1 and key > parent.leftChild.key:
            parent.leftChild = parent.leftRotate(parent.leftChild)
            return parent.rightRotate(parent)

        return parent


    def getHeight(self,parent):
        if parent is None:
            return 0
        return parent.height


    def Balance(self,parent):
        if parent is None:
            return 0

        ## AVLTree equation to calculate the balance of a node
        ## used to choose rotation method 
        return self.getHeight(parent.leftChild) - self.getHeight(parent.rightChild)
    

    def rotateRight(self, parent):
        ## set a ref for soon to be parent
        ref = parent.leftChild

        ## set ref for soon to be child  
        childLeft = ref.rightChild

        ## swap places
        parent.rightChild = parent
        childLeft = parent.leftChild

        ## calculate new heights for balance 
        parent.height = 1 + max(self.getHeight(parent.leftChild),(self.getHeight(parent.rightChild)))
        ref.height = 1 + max(self.getheight(ref.leftChild),self.getHeight(ref.rightChild))

        return a
        

    def rotateLeft(self, parent):
        ## set a ref for the soon to be parent 
        ref = parent.rightChild

        ## set a reference for the soon to be child 
        childLeft = ref.leftChild 

        ## switch places 
        ref.leftChild = parent
        parent.rightChild = childLeft

        ## calc new heights
        parent.height = 1 + max(self.getHeight(parent.leftChild),(self.getHeight(parent.rightChild)))
        ref.height = 1 + max(self.getHeight(ref.leftChild),self.getHeight(ref.rightChild))

        return ref
        
Tree = AVLTree()
root = None
root = Tree.insert(root, 1)
root = Tree.insert(root, 2)
root = Tree.insert(root, 3)
root = Tree.insert(root, 4)
root = Tree.insert(root, 5)
root = Tree.insert(root, 6)
