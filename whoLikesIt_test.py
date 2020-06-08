import unittest
from whoLikesIt import likes

class LikesTest(unittest.TestCase):
    def test_no_one_likes_this(self):
        self.assertEqual(likes([]), 'no one likes this')

    def test_a_single_likes_this(self):
        self.assertEqual(likes(['Peter']), 'Peter likes this')

    def test_double_like_this(self):
        self.assertEqual(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')

    def test_three_like_this(self):
        self.assertEqual(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')

    def test_more_like_this(self):
        self.assertEqual(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')

if __name__ == "__main__":
    unittest.main()