"""
test_base
----------------------------------

Tests for `barrowman.__init__` module.
"""

import unittest
import barrowman
from math import degrees

class TestBase(unittest.TestCase):

    def test_fin_sweep(self):
        """See that sweep and sweepangle are correctly created depending on how
        it's specified.
        """

        # four possibilities:

        # 1.) Define sweep angle
        fin = barrowman.Fin(0.2, 0.05, 0.1, sweepangle=45.0)
        self.assertAlmostEqual(fin.sweep, 0.1, 8)
        self.assertAlmostEqual(degrees(fin.sweepangle), 45.0, 8)

        # 2.) Define sweep
        fin = barrowman.Fin(0.2, 0.05, 0.1, sweep=0.1)
        self.assertAlmostEqual(fin.sweep, 0.1, 8)
        self.assertAlmostEqual(degrees(fin.sweepangle), 45.0, 8)

        # 3.) Define both
        fin = barrowman.Fin(0.2, 0.05, 0.1, sweep=0.1, sweepangle=45.0)
        self.assertAlmostEqual(fin.sweep, 0.1, 8)
        self.assertAlmostEqual(degrees(fin.sweepangle), 45.0, 8)

        # 4.) Define neither (defaults to 45 degrees)
        fin = barrowman.Fin(0.2, 0.05, 0.1)
        self.assertAlmostEqual(fin.sweep, 0.1, 8)
        self.assertAlmostEqual(degrees(fin.sweepangle), 45.0, 8)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
