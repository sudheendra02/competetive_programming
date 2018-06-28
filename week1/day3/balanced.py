class binarytree(object):
	class node(object):
		def __init__(self,object):
			self.data=object
			self.left=None
			self.right=None
	def height(root):
		if root is None:
			return 0
		return max(height(root.left),height(root.right))+1
	def isbalanced(root):
		if root is None:
			return True
		if abs(height(root.left)-height(root.right))<=1 and isbalanced(root.left) and isbalanced(root.right) :
			return True
		return False

