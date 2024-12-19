"""
Name: Amanda Hoelting
Title: Max Heap
"""
import math
class max_heap(object):
    """Binary max-heap

    Supports most standard heap operations (insert, peek, extract_max).
    Can be used for building a priority queue or heapsort. Since Python
    doesn't have built-in arrays, the underlying implementation uses a
    Python list instead. When initialized, max_heap creates a new list of
    fixed size or uses an existing list.

    Attributes
    ----------
    max_size : int or float
        Maximum size of the heap
    length: int or float
        Current length of the heap
    heap: List of integers
        Represents the values in a max heap

    """

    def __init__(self, size = 20, data = None):
        """Initialize a binary max-heap.

        size: Total capacity of the heap.
        data: List containing the desired heap contents. 
              The list is used in-place, not copied, so its contents 
              will be modified by heap operations -- using __swap method.
              If data is specified, then the size field is ignored."""

        # Add to this constructor as needed
        if data is not None:
            self.max_size = len(data)
            self.length = len(data)
            self.heap = data
        else:
            self.max_size = size
            self.length = 0
            self.heap = [None] * size
        
    def get_heap(self):
        """Returns self.heap"""
        return self.heap


    def insert(self, data):
        """Insert an element into the heap.

        data: An integer that will be inserted into the max heap.

        Raises IndexError if the heap is full."""
        if (self.length + 1) > self.max_size:
            raise IndexError
        self.heap[self.length] = data
        self.length += 1

        pos = self.length - 1
        while (pos > 0):
            if (self.heap[pos] > self.heap[self.__get_parent(pos)]):
                self.__swap(pos, self.__get_parent(pos))
            pos = self.__get_parent(pos)




        
    def peek(self):
        """Return the maximum value in the heap."""
        return self.heap[0]

    def extract_max(self):
        """Remove and return the maximum value in the heap.

        Raises KeyError if the heap is empty."""
        
        if self.length < 1:
            raise KeyError
        temp = self.heap[0]
        self.heap[0] = self.heap[self.length-1]
        self.heap[self.length - 1] = temp
        max = self.heap.pop(self.length-1)
        self.length -= 1
        self.__heapify(0)
        return max

    def sort_in_place(self):
        """Perform heapsort in-place (e.g., reorder elements in ascending order for self.heap).
        """
        self.build_heap()
        g = self.length - 1
        for i in range(self.length - 1):
            r = g - i
            self.__swap(0, r)
            self.length -= 1
            self.__heapify(0)



    def __heapify(self, curr_index, list_length = None):
        """Moves elements down in the heap so curr_index and its children are a valid heap.
        Raises IndexError if the heap is full.

        curr_index: Index of element we are checking to see if
        it follows heap properties.
        list_length: Set to none automatically, but can be set to different
        value than self.length.
        """
        # helper function for moving elements down in the heap
        # Page 157 of CLRS book
        if list_length == None:
            list_length = self.length
        if curr_index > self.max_size:
            raise IndexError
        left = self.__get_left(curr_index)
        right = self.__get_right(curr_index)
        if (left < list_length) and (self.heap[left] > self.heap[curr_index]):
            largest = left
        else:
            largest = curr_index
        if (right < list_length) and (self.heap[right] > self.heap[largest]):
            largest = right
        if largest != curr_index:
            self.__swap(curr_index, largest)
            self.__heapify(largest)



    def build_heap(self):
        """Builds a heap using the __heapify helper function

        """
        for i in range(math.floor(self.length/2) + 1):
            r = math.floor(self.length / 2) - i
            self.__heapify(r)


    def __get_parent(self, loc):
        """Returns the parent index of a child in the heap

        loc: Index of the child element.
        """
        # left child has odd location index
        # right child has even location index
        if loc % 2 == 0:
            parent = int((loc - 2) / 2)
        else:
            parent = int((loc - 1) / 2)
        return parent

    def __get_left(self, loc):
        """Returns the left child of a parent index.

        loc: Index of the parent element.
        """
        return 2*loc + 1

    def __get_right(self, loc):
        """Returns the right child of a parent index.

        loc: Index of the parent .
        """
        return 2*loc + 2
        

    def __swap(self, a, b):
        """Swap elements located at indexes a and b of the heap.

        a: Index of a element in the heap.
        b: Index of another element in the heap.
        """
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp
    

def heap_sort(l):
    """The public heap_sort should do the following.
    1. Create a max_heap object using the provided list l
    2. Call sort_in_place method to sort the list "in-place"
    """
    heap = max_heap(len(l), l)
    heap.sort_in_place()
    return heap.get_heap()

