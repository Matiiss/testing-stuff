import unittest

import le_test as lt


class TestTyping(unittest.TestCase):
    def test_duck_protocol(self):
        self.assertTrue(hasattr(lt.typing.Duck, "walk"))
        self.assertTrue(hasattr(lt.typing.Duck, "quack"))


if __name__ == '__main__':
    unittest.main()
