from LRU import LRU

import unittest

class LRUTest(unittest.TestCase):
    l = LRU(4)
    l.put(1)
    l.put(2)
    l.put(3)
    l.put(4)
    l.put(5)
    l.put(5)
    l.put(6)
    def test1(self):
        self.assertEqual(self.l.get_cache(),[3,4,5,6])
    def test3(self):
        self.assertEqual(self.l.get(),3)

if __name__ == '__main__':
   unittest.main()

