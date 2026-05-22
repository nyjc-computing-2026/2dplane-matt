

def _hash_key(key: str, p: int = 53) -> int:
    """Hashes the key using the rolling polynomial algorithm.

    Arguments:
    - key: str
      The key to be hashed.
    - p: int
      A prime number used for the rolling polynomial algorithm

    Returns:
    - the hashed location (int)
    """
    total = 0
    for i, char in enumerate(key):
        total += ord(char) * p**i
    return total


class HashTable:
    """A hashtable without collision resolution.

    Arguments:
    - size: int
      The number of slots that the hash table is initialised with

    Attributes:
    - size: int
      The number of slots that the hash table has
    - length: int
      The number of records contained in the hash table
    """

    def __init__(self, size: int):
        self.size = size               # total number of slots for data to be stored in hashtable
        self.length = 0                # current number of keys in hashtable
        self._data = [None] * size     # the empty hashtable where the data will be stored
        # Add your code here

    def __repr__(self) -> str:
        return f"HashTable(size={self.size})" 

    def setitem(self, key: str, value: dict) -> None:
        """Stores key and value in the hash table.

        If the key already exists in the hash table, the existing value
        is overwritten.
        """
        index = _hash_key(key) % self.size
        start = index
        while (index + 1) % self.size != start:
            if self._data[index] is None:
                self._data[index] = (key, value)
                self.length += 1

        

    def getitem(self, key: str) -> dict:
        """Retrieves the value associated with key, and returns it.

        If the key does not exist, a KeyError is raised.
        """
        index = _hash_key(key)
        if index >= self.length:
            index = index % self.size
        if self._data[index] is None:
            raise KeyError('Key does not exist')
        else:
            return self._data[index]
            

    def delitem(self, key: str) -> None:
        """Deletes the key and its associated value from the hash table.

        If the key does not exist, a KeyError is raised.
        """
        index = _hash_key(key)
        if index >= self.length:
            index = index % self.size
        if self._data[index] is None:
            raise KeyError('Key does not exist')
        self._data[index] = None
        
        

class HashTableLinearProbing(HashTable):
    """A hashtable that implements collision resolution using
    linear probing.

    Arguments:
    - size: int
      The number of slots that the hash table is initialised with
    """

    def __init__(self, size: int):
        super().__init__(size)

        # Add your code here

    def __repr__(self) -> str:
        return f"HashTableLinearProbing(size={self.size})"

    def setitem(self, key: str, value: dict) -> None:
        """Stores key and value in the hash table.

        If the key already exists in the hash table, the existing value
        is overwritten.
        """
        index = _hash_key(key) % self.size
        start = index
        while (index + 1) % self.size != start:
            if self._data[index] is None:
                self._data[index] = (key, value)
                self.length += 1

            existingkey = self._data[index]
            if existingkey == key:
                return
            self._data[index] = (key, value)

    def getitem(self, key: str) -> dict:
        """Retrieves the value associated with key, and returns it.

        If the key does not exist, a KeyError is raised.
        """
        index = _hash_key(key) % self.size
        start = index
        while (index + 1) % self.size != start:
            if self._data[index] is None:
                raise KeyError

            existingkey = self._data[index]
            if existingkey == key:
                return self._data[index]
            
            index += 1

    def delitem(self, key: str) -> None:
        """Deletes the key and its associated value from the hash table.

        If the key does not exist, a KeyError is raised.
        """
        raise NotImplementedError

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def setkey(self,key,value):
        node = Node(key, value)
        if not self.head:
            self.head = node
            return
        
        current = self.head
        while current.next is not None:  # check till u reach None at the end
            if current.key != key:       # if key doesnt exxist,just write on next empty gap
                current = current.next
            else:
                current.value = value    # if key alr exists overwrite the value
                return
        current.next = node

    def getkey(self,key):
        if not self.head:
            raise KeyError
        
        current = self.head

        while current.next is not None:
            if current.key == key:        # its the key of current so its an attribute
                return current.value
        raise KeyError
    
    def delkey(self,key):
        if not self.head:
            raise KeyError
        elif self.head.key == key:
            self.head = self.head.next
            return 

        previous = self.head
        current = self.head.next

        while current is not None:
            if current.key == key:
                previous.next = current.next
                return 
            previous = current
            current = current.next
        raise KeyError
    
                




        

    

class HashTableSeparateChaining(HashTable):
    """A hashtable that implements collision resolution using
    separate chaining.

    Arguments:
    - size: int
      The number of slots that the hash table is initialised with
    """

    def __init__(self, size: int):
        super().__init__(size)
        for i in range(self.size):
            self._data[i] = LinkedList()

    def __repr__(self) -> str:
        return f"HashTableLinearProbing(size={self.size})"

    def setitem(self, key: str, value: dict) -> None:
        """Stores key and value in the hash table.

        If the key already exists in the hash table, the existing value
        is overwritten.
        """
        index = _hash_key(key)
        self._data[index].setkey(key, value)

    def getitem(self, key: str) -> dict:
        """Retrieves the value associated with key, and returns it.

        If the key does not exist, a KeyError is raised.
        """
        index = _hash_key(key)
        return self._data[index].getkey(key)

    def delitem(self, key: str) -> None:
        """Deletes the key and its associated value from the hash table.

        If the key does not exist, a KeyError is raised.
        """
        index = _hash_key(key)
        self._data[index].delkey(key)
