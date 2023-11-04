# README for Tree Data Structures

This repository contains implementations of three different tree data structures in Python: BinaryTree, MaxHeap, and AVLTree. Each class provides its own set of methods to interact with the tree structure it represents.

## General Info 
Each tree structure is implemented as a class that contains the relevant methods for manipulating and querying the tree. The trees are generic and can be used with any comparable data type.

Please refer to the comments in each class file for more detailed instructions on how each method functions and any expected parameters.

## Reqs 
Python 3.x

## BinaryTree

The BinaryTree class is a basic binary tree implementation with the ability to insert left and right children, and retrieve the left child, right child, and root values of the tree. It also provides a method CheckBST to validate whether a given binary tree is a binary search tree.

## Usage 
```
from BinaryTree import BinaryTree, CheckBST

# Create a binary tree with a root node
btree = BinaryTree(8)
btree.insertRight(6)
btree.insertLeft(4)
btree.insertRight(9)
btree.insertLeft(7)

# Check if the binary tree is a binary search tree
is_bst = CheckBST(btree)
print("Is BST:", is_bst)
```

## MaxHeap
The MaxHeap class represents a max-heap data structure where the parent node is always greater than its children. It supports insertion of elements and provides methods to find and delete the maximum element in the heap.

## Usage 
```
from MaxHeap import MaxHeap

# Create a max heap
heap = MaxHeap()

# Insert elements into the heap
heap.insert(3)
heap.insert(5)
heap.insert(6)
heap.insert(10)
heap.insert(15)
heap.insert(23)
heap.insert(90)

# Find and delete the maximum element
max_element = heap.findMax()
print("Max Element:", max_element)
heap.delMax()
```
## AVLTree
The AVLTree class implements an AVL tree, which is a self-balancing binary search tree. The balance of the tree is maintained through rotations after every insertion operation.

## Usage 
```
from AVLTree import AVLTree

# Create an AVL tree and insert elements
avl_tree = AVLTree()
root = None
root = avl_tree.insert(root, 1)
root = avl_tree.insert(root, 2)
root = avl_tree.insert(root, 3)
root = avl_tree.insert(root, 4)
root = avl_tree.insert(root, 5)
root = avl_tree.insert(root, 6)
```

## Author 
Harrison Heath 
