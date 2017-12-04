import unittest

class TestStringMethods(unittest.TestCase):
    def test_sorted(self):
        self.assertEqual(remove_negs([1,5,9,2,8]), [1,2,5,8,9])
        self.assertEqual(remove_negs([1,8,'a','y', 'c']), [1,8,'a','c','y'])

    def test_remove_negs(self):
        self.assertEqual(remove_negs([1,-5,9,2,8]), [1,2,8,9])
        self.assertEqual(remove_negs([1,-2,0,'a', 'b','hi']), [0,1,'a','b', 'hi'])

def remove_negs(a):
    lst = sorted([str(x) for x in a])
    fin = []
    for i in lst:
        try:
            num = int(i)
            if num < 0:
                pass
            else:
                fin.append(int(i))

        except:
            fin.append(i)
    return fin

if __name__ == '__main__':
    unittest.main()
