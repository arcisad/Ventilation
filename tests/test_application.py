import unittest
import inspect

from sources import ven
from ven import TLC, FRC


class ApplicationTests(unittest.TestCase):
    def test_application(self):
        self.assertTrue(inspect.ismodule(ven))

if __name__ == '__main__':
    unittest.main()
