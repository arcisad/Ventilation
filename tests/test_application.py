import unittest
import inspect


from sources import ven
from sources.ven import FRC, TLC


class ApplicationTests(unittest.TestCase):
    def test_application(self):
        self.assertTrue(inspect.ismodule(ven))

    def test_calculate(self):
        value1 = float(FRC.get())
        value2 = float(TLC.get())
        vc = value2 - value1/2
        self.assertEqual(vc, 6)

if __name__ == '__main__':
    unittest.main()
