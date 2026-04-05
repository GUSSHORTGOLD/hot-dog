import unittest
from dirty_hotdog import HotDog

class TestHotDog(unittest.TestCase):
    def test_hotdog_creation(self):
        dog = HotDog()
        self.assertTrue(dog.is_dirty)
        self.assertEqual(dog.grease, 100)

    def test_add_ketchup(self):
        dog = HotDog()
        dog.add_ketchup(50)
        self.assertEqual(dog.ketchup, 50)

if __name__ == '__main__':
    unittest.main()
