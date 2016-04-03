#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_original
----------------------------------

Tests for `barrowman.original` module.
"""

import unittest
import barrowman
from barrowman import original


class TestOrignal(unittest.TestCase):

    nose = barrowman.Nose(barrowman.Nose.CONE, 0.1, 0.3)
    tube = barrowman.Tube(0.1, 1.0)
    fin = barrowman.Fin(0.2, 0.05, 0.1, sweepangle=45.0)
    body = original.Body([nose, tube])
    tail = original.Tail(fin, 4)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_body_cp_subsonic(self):
        """Set up a standard rocket (see data/standard-rocket.ork) and find the
        C_P of the body (everything except fins)
        """
        self.assertAlmostEqual(self.body.C_P(0.3), 0.2, places=4)

    def test_tail_cp_subsonic(self):
        """Set up a standard rocket (see data/standard-rocket.ork) and find the
        C_P of the tail (just fins)
        """

        self.assertAlmostEqual(self.tail.C_P(0.3), 0.075, places=4)  #: FIXME Placeholder test, find real number

    def test_rocket_cp_subsonic(self):
        r = original.Rocket(self.body, self.tail)
        self.assertAlmostEqual(r.C_P(0.3), 0.275, places=4)  #: FIXME Placeholder test, find real number

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
