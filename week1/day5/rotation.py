import unittest

def rotate(words,l,h):
    mid = int((l+h)/2)
    # print(mid)
    # if(words[l][0]>words[h][0]):
    if((words[mid])>(words[h])):
        # print("hii")
        return rotate(words,mid+1,h)
    elif((words[mid])<(words[h])):
        # print("bye")
        return rotate(words,l,mid)
    elif(words[mid]==words[h]):
        # print("am here")
        return h
    # else:
    #     return l
    return -1    

def find_rotation_point(words):

    # Find the rotation point in the list
    return rotate(words,0,len(words)-1)



















# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)