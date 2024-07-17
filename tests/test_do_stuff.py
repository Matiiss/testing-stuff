import unittest

import le_test as lt


class TestDoStuff(unittest.TestCase):
    def test_do_stuff(self):
        name = "Jimmy"
        ducky = lt.create_duck(name)

        self.assertEqual(ducky.name, name)
        self.assertIsInstance(ducky, lt.typing.Duck)


if __name__ == "__main__":
    unittest.main()
