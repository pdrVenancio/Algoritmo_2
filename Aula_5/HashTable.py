import BinaryTree as bt

class HashTable:
	def __init__(self, size):
		self.size = size
		self.slots = [None for i in range(size)]
		self.count = 0
	
	def _hash(self, key):
		cont = 1
		valor = 0
		for c in key:
			valor = valor + (ord(c) * cont)
			cont = cont + 1
		return valor % self.size
		
	def put(self, key, value):
		hashValue = self._hash(key)
		position = hashValue
		if self.slots[position] == None:
			self.slots[position] = bt.BinaryTree(key, value)
		else:
			self.slots[position].put(key, value)

	
	# percorrer a tabela hash
	def get_has(self, key):
		hashValue = self._hash(key)
		position = hashValue
		# self.slots[position] é do tipo BinaryTree
		if self.slots[position] is not None:
			return self.slots[position].get_bt(key)
		return None
		
	def __setitem__(self, key, value):
		self.put(key, value)
	
	def __getitem__(self, key):
		return self.get_has(key)
		
		






































