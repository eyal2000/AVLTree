# AVLTree

Python implementation of a self-balancing AVL tree.  

Supports the following operations:

- **Constructor**  
  `AVLTree()`  
  Create an empty AVL tree.

- **Insertion**  
  `insert(key, value)`  
  Insert a new node with the given key and value; returns the number of rotations performed.

- **Deletion**  
  `delete(node)`  
  Remove the specified node; returns the number of rotations performed.

- **Search**  
  `search(key)`  
  Return the node with the matching key, or `None` if not found.

- **Size**  
  `size()`  
  Return the total count of real nodes in the tree.

- **Traversal**  
  `avl_to_array()`  
  Return an in-order list of all `(key, value)` pairs.  

- **Split**  
  `split(node)`  
  Partition the tree into two AVL trees: one with all keys less than `node.key`, the other with all keys greater.

- **Join**  
  `join(other_tree, key, value)`  
  Merge the current tree with other_tree by inserting the given key and value between them; returns the number of rotations performed.  
  *(Requires that all keys in other_tree are either strictly less than or strictly greater than key.)*

- **Root Access**  
  `get_root()`  
  Return the current root node of the tree.
