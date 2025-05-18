"""
A class represnting a node in an AVL tree
"""
class AVLNode(object):
	"""Constructor, you are allowed to add more fields.

	@type key: int or None
	@type value: any
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.bf = 0
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1


	"""returns the bf
	@rtype: int
	@returns: the bf of self
	"""
	def get_bf(self):
		return self.bf


	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	def get_left(self):
		return self.left


	"""returns the right child
	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self):
		return self.right


	"""returns the parent 
	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def get_parent(self):
		return self.parent


	"""returns the key
	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	def get_key(self):
		return self.key


	"""returns the value
	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	def get_value(self):
		return self.value


	"""returns the height
	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def get_height(self):
		return self.height


	"""sets bf
	@type bf: int
	@param bf: bf
	"""
	def set_bf(self, bf):
		self.bf = bf
		return None


	"""sets left child
	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node):
		self.left = node
		return None


	"""sets right child
	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node):
		self.right = node
		return None


	"""sets parent
	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node):
		self.parent = node
		return None


	"""sets key
	@type key: int or None
	@param key: key
	"""
	def set_key(self, key):
		self.key = key
		return None


	"""sets value
	@type value: any
	@param value: data
	"""
	def set_value(self, value):
		self.value = value
		return None


	"""sets the height of the node
	@type h: int
	@param h: the height
	"""
	def set_height(self, h):
		self.height = h
		return None


	"""returns whether self is not a virtual node
	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		if self.height == -1:
			return False
		return True


	"""
	turns node into a leaf
	creates two virtual nodes for a new inserted leaf & update height and BF accordingly
	"""
	def leaf(self):
		self.bf = 0
		self.height = 0
		self.left = AVLNode(None, None)
		self.left.parent = self
		self.right = AVLNode(None, None)
		self.right.parent = self


	"""
	update height and BF according to left & right children
	"""
	def update_node(self):
		self.set_height(1 + max(self.right.height, self.left.height))
		self.set_bf(self.left.height - self.right.height)


"""
A class implementing the ADT Dictionary, using an AVL tree.
"""
class AVLTree(object):

	"""
	Constructor
	"""
	def __init__(self):
		self.root = AVLNode(None, None)
		self.t_size = 0


	"""
	searches for an AVLNode in the dictionary corresponding to the key
	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: the parent of the supposed position of the AVLNode corresponding to the key
	@complexity: O(log(n))
	"""
	def tree_position(self, key):  # returns the parent of the location the inserted key would be in
		node = self.root
		while node.height >= 0:
			if node.key == key:
				return node
			elif node.key < key:
				node = node.right
			else:
				node = node.left
		return node.parent


	"""
	perform a right rotation on the node
	@type x: node
	@param x: a node to be rotated
	@complexity: O(1)
	"""
	def rot_right(self, x):
		parent = x.parent
		y = x.left

		if parent is None:
			self.root = y
		else:
			if x.key > parent.key:
				parent.right = y
			else:
				parent.left = y
		y.parent = parent

		x.left = y.right
		x.left.parent = x

		y.right = x
		x.parent = y

		x.update_node()
		y.update_node()

		if parent:
			parent.update_node()


	"""
	perform a left rotation on the node
	@type x: node
	@param x: a node to be rotated
	@complexity: O(1)
	"""
	def rot_left(self, y):
		parent = y.parent
		x = y.right

		if parent is None:
			self.root = x
		else:
			if y.key > parent.key:
				parent.right = x
			else:
				parent.left = x
		x.parent = parent

		y.right = x.left
		y.right.parent = y

		x.left = y
		y.parent = x

		y.update_node()
		x.update_node()

		if parent:
			parent.update_node()


	"""
	searches for the successor of a node
	@type node: node
	@param node: the node we'll receive the successor of
	@rtype: AVLNode
	@returns: the successor of the node
	@complexity: O(log(n))
	"""
	def successor(self, node):
		if node.right.is_real_node():
			node = node.right
			while node.left.is_real_node():
				node = node.left
			return node
		else:
			parent = node.parent
			while parent and node == parent.right:
				node = parent
				parent = node.parent
			return node.parent


	"""
	searches for a AVLNode in the dictionary corresponding to the key
	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: the AVLNode corresponding to key or None if key is not found.
	@complexity: O(log(n))
	"""
	def search(self, key):
		node = self.root
		while node.height >= 0:
			if node.key == key:
				return node
			elif node.key < key:
				node = node.right
			else:
				node = node.left
		return None


	"""
	inserts val at position i in the dictionary
	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	@complexity: O(log(n))
	"""
	def insert(self, key, val):
		self.t_size += 1
		node = AVLNode(key, val)
		node.leaf()
		if not self.root.is_real_node():  # if the tree is empty
			self.root = node
			return 0
		parent = self.tree_position(key)
		node.set_parent(parent)
		if key > parent.key:
			parent.set_right(node)
		else:
			parent.set_left(node)
		counter = 0
		while parent is not None:
			pre_h = parent.height
			parent.update_node()
			if abs(parent.bf) < 2 and parent.height == pre_h:  # BF is fine and parent height has not changed
				return counter
			elif abs(parent.bf) < 2 and parent.height != pre_h:  # BF is fine but parent height has changed
				parent = parent.parent
				counter += 1
			else:  # BF is two, doing one rotation (or double rotation) to achieve BF of one (same as pre insertion)
				if parent.bf > 0:
					if parent.left.bf == -1:
						self.rot_left(parent.left)
						counter += 1
					self.rot_right(parent)
				else:
					if parent.right.bf == 1:
						self.rot_right(parent.right)
						counter += 1
					self.rot_left(parent)
				return counter + 1
		return counter


	"""
	deletes node from the dictionary
	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	@complexity: O(log(n))
	"""
	def delete(self, node):
		self.t_size -= 1
		parent = self.delete_bst(node)  # delete as in BST
		counter = 0
		while parent:
			pre_h = parent.height
			parent.update_node()
			if abs(parent.bf) < 2 and parent.height == pre_h:  # BF is fine and parent height has not changed
				return counter

			elif abs(parent.bf) < 2 and parent.height != pre_h:  # BF is fine but parent height has changed
				parent = parent.parent
				counter += 1

			else:  # BF is two, doing one rotation (or double rotation) to achieve BF of one (same as pre insertion)
				next_parent = parent.parent
				if parent.bf > 0:
					if parent.left.bf == -1:
						self.rot_left(parent.left)
						counter += 1
					self.rot_right(parent)
				else:
					if parent.right.bf == 1:
						self.rot_right(parent.right)
						counter += 1
					self.rot_left(parent)
				parent = next_parent
				counter += 1
		return counter


	"""
	deletes node from the AVLTree
	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: AVLNode
	@returns: the parent of the physically deleted node
	@complexity: O(log(n)) Worse case
	"""
	def delete_bst(self, node):
		v_node = AVLNode(None, None)
		return_node = node.parent
		if node.height == 0:  # node is a leaf
			if node == self.root:
				self.root = v_node
			else:
				if node.parent.right == node:
					node.parent.right = v_node
				else:
					node.parent.left = v_node
			v_node.parent = node.parent

		elif node.left.is_real_node() and not node.right.is_real_node():  # node has only left child
			if node == self.root:
				self.root = node.left
			else:
				if node.parent.right == node:
					node.parent.right = node.left
				else:
					node.parent.left = node.left
			node.left.parent = node.parent

		elif not node.left.is_real_node() and node.right.is_real_node():  # node has only right child
			if node == self.root:
				self.root = node.right
			else:
				if node.parent.right == node:
					node.parent.right = node.right
				else:
					node.parent.left = node.right
			node.right.parent = node.parent

		else:  # node has both left & right children
			suc_node = self.successor(node)
			self.delete_bst(suc_node)

			if suc_node.parent == node:
				return_node = suc_node
			else:
				return_node = suc_node.parent

			suc_node.left = node.left
			node.left.parent = suc_node

			suc_node.right = node.right
			node.right.parent = suc_node

			suc_node.parent = node.parent
			if self.root == node:
				self.root = suc_node
			else:
				if node.parent.right == node:
					suc_node.parent.right = suc_node
				else:
					suc_node.parent.left = suc_node

			suc_node.update_node()

		return return_node


	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	@complexity: O(n)
	"""
	def avl_to_array(self):
		arr = []
		curr = self.root
		stack = []
		while stack or curr.is_real_node():
			if curr.is_real_node():
				stack.append(curr)
				curr = curr.left
			else:
				curr = stack.pop()
				arr.append((curr.get_key(), curr.get_value()))
				curr = curr.right
		return arr


	"""
	returns the number of items in dictionary 
	@rtype: int
	@returns: the number of items in dictionary 
	@complexity: O(1)
	"""
	def size(self):
		return self.t_size


	"""
	splits the dictionary at the i'th index
	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	@complexity: O(log(n))
	"""
	def split(self, node):
		t1 = AVLTree()
		t2 = AVLTree()
		arr = [t1, t2]

		t1.root = node.left
		t1.root.parent = None

		t2.root = node.right
		t2.root.parent = None

		tree = AVLTree()

		parent = node.parent
		while parent:
			if parent.right is node:
				tree.root = parent.left
				tree.root.parent = None

				t1.join(tree, parent.get_key(), parent.get_value())

			else:
				tree.root = parent.right
				tree.root.parent = None

				t2.join(tree, parent.get_key(), parent.get_value())

			node = parent
			parent = parent.parent

		return arr


	"""
	joins self with key and another AVLTree
	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree2
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	@complexity: O(log(n)) worst case
	"""
	def join(self, tree2, key, val):

		diff = abs(self.root.get_height() - tree2.root.get_height()) + 1
		self.t_size += tree2.t_size + 1
		mid = AVLNode(key, val)
		mid.leaf()

		if not self.root.is_real_node() and not tree2.root.is_real_node():
			self.root = mid
			return diff

		elif not tree2.root.is_real_node():
			self.insert(key, val)
			return diff

		elif not self.root.is_real_node():
			tree2.insert(key, val)
			self.root = tree2.root
			return diff

		if self.root.key > tree2.root.key:
			small = tree2.root
			big = self.root
		else:
			small = self.root
			big = tree2.root

		if big.get_height() >= small.get_height():
			self.root = big
			while big.get_height() > small.get_height():
				big = big.left

			parent = big.parent

			if not parent:
				self.root = mid
			else:
				parent.left = mid

		else:
			self.root = small
			while small.get_height() > big.get_height():
				small = small.right

			parent = small.parent

			if not parent:
				self.root = mid
			else:
				parent.right = mid

		mid.parent = parent

		mid.left = small
		small.parent = mid

		mid.right = big
		big.parent = mid

		mid.update_node()

		while parent:
			pre_h = parent.height
			parent.update_node()
			if abs(parent.bf) < 2 and parent.height == pre_h:  # BF is fine and parent height has not changed
				return diff
			elif abs(parent.bf) < 2 and parent.height != pre_h:  # BF is fine but parent height has changed
				parent = parent.parent
			else:  # BF is two, doing one rotation (or double rotation) to achieve BF of one (same as pre insertion)
				next_parent = parent.parent
				if parent.bf > 0:
					if parent.left.bf == -1:
						self.rot_left(parent.left)
					self.rot_right(parent)
				else:
					if parent.right.bf == 1:
						self.rot_right(parent.right)
					self.rot_left(parent)
				parent = next_parent
		return diff


	"""
	returns the root of the tree representing the dictionary
	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	@complexity: O(1) worst case
	"""
	def get_root(self):
		return self.root
