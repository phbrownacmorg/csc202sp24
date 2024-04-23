import unittest
# import the code you want to test here
from Hashtable import Hashtable

class TestHashtable(unittest.TestCase):

    def setUp(self) -> None:
        self._empty = Hashtable()

        self._keys = ['Zelle', 'Brown', 'Maher', 'Kharb']
        self._letterhashes = [60, 72, 45, 40, 69, 112, 88, 119]
        self._values = ['John Zelle', 'Peter Brown', 'Caleb Maher', 'Khushi Kharb']
        self._not_keys = ['Smith', 'Benderskyi', 'Davidson', 'Merrithew']
        self._keylist = self._keys + self._not_keys

        self._4 = Hashtable()
        for i in range(len(self._keys)):
            self._4.put(self._keys[i], self._values[i])
        self._4hashes = [0, 0, 1, 0, 1, 0, 0, 3]

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testLetterhash(self) -> None:
        for i in range(len(self._keylist)):
            with self.subTest(i=i):
                self.assertEqual(Hashtable.letterhash(self._keylist[i]), self._letterhashes[i])

    def testHash(self) -> None:
        for i in range(len(self._keylist)):
            with self.subTest(i=i):
                self.assertEqual(self._empty._hash(self._keylist[i]), self._4hashes[i])

    def testContains(self) -> None:
        for name in self._keys:
            with self.subTest(name=name):
                self.assertFalse(name in self._empty)
                self.assertTrue(name in self._4)

        for name in self._not_keys:
            with self.subTest(name=name):
                self.assertFalse(name in self._empty)
                self.assertFalse(name in self._4)

    def testGet(self) -> None:
        for i in range(len(self._keys)):
            with self.subTest(i=i):
                self.assertEqual(self._4.get(self._keys[i]), self._values[i])
                with self.assertRaises(KeyError):
                    self._empty.get(self._keys[i])
        # Just for paranoia: do I get the proper error when the table's not empty?
        for i in range(len(self._not_keys)):
            with self.subTest(i=i):
                with self.assertRaises(KeyError):
                    self._4.get(self._not_keys[i])


if __name__ == '__main__':
    unittest.main()

