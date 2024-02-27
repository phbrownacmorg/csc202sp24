import unittest
# import the code you want to test here

from baseconvert import changebase, digits
class TestNothing(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testTrue(self) -> None:
        self.assertTrue(True)

    def test_convert(self) -> None:
        for base in [2, 8, 10, 12, 16]:
            for i in range(base):
                for j in range(base):
                    with self.subTest(i=i, j=j):
                        if i > 0:
                            expected = digits[i] + digits[j]
                        else:
                            expected = digits[j]
                        print(base, i * base + j, changebase(i * base + j, base), expected)
                        self.assertEqual(changebase(i * base + j, base), expected)

if __name__ == '__main__':
    unittest.main()

