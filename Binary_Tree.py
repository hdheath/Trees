class BinaryTree:

    def __init__(self,rootObj):

        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        
        if self.leftChild == None:

            self.leftChild = BinaryTree(newNode)
        
        else:

            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        
        if self.rightChild == None:

            self.rightChild = BinaryTree(newNode)
            
        else:

            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
    
        

def CheckBST(btree) :

    ## if tree is empty return true
    if btree.key is None:
        return True

    ## create variable names for 
    a = btree.getLeftChild()
    b = btree.getRightChild()
    c = BinaryTree(btree.getRootVal())
    d = BinaryTree(btree.getRootVal())
    e = a
    f = b

    if a is None and b is None and e is None and f is None:
        return True

    else:
        
        ## if the value of the left child is greater than the parent value
        ## or the value of the right child is less than the parent value :
        ## return False (disobeys rules for BST)
        if a.key > c.key or b.key < c.key :
            return False

        
        elif e.key < d.key  or f.key < d.key :
            return False

        ## if the prior values are accepted
        ## create a new node data type and append the children of the next parent 
        else:
            c.__init__(a.key) 
            c.insertLeft(a.getLeftChild())
            c.insertRight(a.getRightChild())
            a = c.getLeftChild()
            b = c.getRightChild()

         ## recursive call to the function to search through the next nodes
            CheckBST(c)

        ## repeat the process for the other child 
            d.__init__(b.key)
            d.insertLeft(b.getLeftChild())
            d.insertRight(b.getRightChild())
            e = d.getLeftChild()
            f = d.getRightChild()

        ## recursive call to the function to search through the next nodes
            CheckBST(d)
                
                
                
                
                
                
h = BinaryTree(8)
h.insertRight(6)
h.insertLeft(4)
h.insertRight(9)
h.insertLeft(7)
CheckBST(h)
        
        

    
        
