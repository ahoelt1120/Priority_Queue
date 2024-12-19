import unittest
import pqueue
import mheap


class T0_pqueue_insert(unittest.TestCase):


    def test_1_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [5,4,2,1,3])
        print("\n")

    def test_2_pq_insert_full(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        with self.assertRaises(IndexError):
            pq.insert(6)
        print("\n")

class T1_pqueue_peek(unittest.TestCase):

    def test_1_pq_peek(self):
        print("Just return the fist element of the queue.")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.peek(), 3)
        print("\n")

class T2_pqueue_extract_max(unittest.TestCase):

    def test_1_pq_extract_max(self):
        print("extract and return the maximum element of the queue")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.extract_max(), 3)
        print("\n")

    def test_2_pq_extract_max_empty(self):
        print("Checks that KeyError is raised for peeking into empty list")
        print("\n")
        pq = pqueue.pqueue(5)
        with self.assertRaises(KeyError):
            pq.extract_max()
        print("\n")

class T4_pqueue_extract_max_and_insert(unittest.TestCase):
    def test_1_pq_insert_extract(self):
        print("insert values and extract max and still get valid heap")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.extract_max()
        pq.extract_max()
        pq.insert(4)
        pq.insert(2)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [4, 1, 2])
        print("\n")
    def test_2_pq_insert_extract_more(self):
        print("insert values and extract max and still get valid heap")
        print("\n")
        pq = pqueue.pqueue(10)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq.extract_max()
        pq.extract_max()
        pq.insert(2)
        pq.insert(1)
        pq.insert(6)
        pq.extract_max()
        pq.insert(7)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [7, 2, 3, 1, 1, 2])
        print("\n")


class T5_build_heap(unittest.TestCase):

    def test_1_build_heap_basic_example(self):
        print("create a heap and use build_heap()")
        print("\n")
        li = [20, 45, 90, 1, 3, 15, 45, 76, 13]
        hp = mheap.max_heap(len(li), li)
        hp.build_heap()
        self.assertEqual(hp.get_heap(), [90, 76, 45, 45, 3, 15, 20, 1, 13])
        print("\n")

    def test_2_build_heap_shorter_example(self):
        print("create a heap and use build_heap()")
        print("\n")
        li = [4,6,7]
        hp = mheap.max_heap(len(li), li)
        hp.build_heap()
        self.assertEqual(hp.get_heap(), [7, 6, 4])
        print("\n")

    def test_3_build_heap_insert_extra(self):
        print("create a heap and use build_heap()")
        print("\n")
        li = [20, 45, 90, 1, 3, 15, 45, 76, 13]
        hp = mheap.max_heap(len(li), li, )
        hp.build_heap()
        with self.assertRaises(IndexError):
            hp.insert(1)

        print("\n")


class T6_heap_sort(unittest.TestCase):

    def test_heap_sort_1(self):
        print("\n")
        to_sort_list = [10,24,3,57,4,67,37,87,7]
        sorted_list = mheap.heap_sort(to_sort_list)

        self.assertEqual(sorted_list, [3, 4, 7, 10, 24, 37, 57, 67, 87])
        print("\n")

    def test_heap_sort_2(self):
        print("\n")
        to_sort_list = [1, 2, 3]
        sorted_list = mheap.heap_sort(to_sort_list)

        self.assertEqual(sorted_list, [1, 2, 3])
        print("\n")
    

    
    
if __name__ == '__main__':
    unittest.main()