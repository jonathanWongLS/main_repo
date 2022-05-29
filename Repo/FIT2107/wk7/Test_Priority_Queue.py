import unittest
from PriorityQueue import PriorityQueue, EmptyQueue

class Test_Priority_Queue(unittest.TestCase):
    # test isEmpty method
    def test_isEmpty(self):
        # test if queue is empty when instantiated
        prio = PriorityQueue()
        prio.add(3, "strawberries")
        self.assertTrue(prio.isEmpty(), "Initial length when list is empty is NOT 0")

    # test isAList method
    def test_isAList(self):
        prio = PriorityQueue()
        self.assertTrue(type(prio.queue) == list, "Queue is not a list")

    # Test add method
    def test_add(self):
        prio = PriorityQueue()
        before = prio.length
        prio.add(3, "strawberries")
        prio.add(1, "banana")
        after = prio.length
        self.assertGreater(after, before, "Add does NOT work")

    # testing .pop() method
    def test_pop(self):
        prio = PriorityQueue()
        prio.add(6, "Samsung")
        prio.add(2, "Apple")
        prio.add(4, "Huawei")
        before = prio.length
        prio.pop()
        after = prio.length
        self.assertNotEqual(before, after, "Pop does NOT work")
        
    # test peek method
    def test_peek(self):
        prio = PriorityQueue()
        prio.add(6, "Samsung")
        prio.add(2, "Apple")
        prio.add(4, "Huawei")
        before = prio.length
        prio.peek()
        after = prio.length
        self.assertEqual(before, after, "Pop does NOT work")

def main():
    # create test suite from the test cases above
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Priority_Queue)
    # run the test suite
    # verbosity is a level of information
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()