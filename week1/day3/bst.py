class node(object):
	def __init__(self,object):
		self.data=object
		self.left,self.right=None,None

min,max=-99999,9999
def isBst(root):
	if root is None:
		return True
	if(root.value<min or root.value>max):
		return False
	if(isBst(root.left,min,root.value-1) and isBst(root.right,root.value+1,max)):
		return True
	return False