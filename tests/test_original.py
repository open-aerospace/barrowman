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

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_body_cp_subsonic(self):
        """Set up a standard rocket (see data/standard-rocket.ork) and find the
        C_P of the body (everything except fins)
        """

        nose = barrowman.Nose(barrowman.Nose.CONE, 0.1, 0.3)
        tube = barrowman.Tube(0.1, 1.0)
        body = original.Body([nose, tube])
        self.assertAlmostEqual(body.C_P(0.3), 0.2, places=4)

    def test_tail_cp_subsonic(self):
        """Set up a standard rocket (see data/standard-rocket.ork) and find the
        C_P of the tail (just fins)
        """

        fin = barrowman.Fin(0.2, 0.05, 0.1, sweepangle=45.0)
        tail = original.Tail(fin, 4)
        self.assertAlmostEqual(tail.C_P(0.3), 0.075, places=4)  #: FIXME Placeholder test, find real number


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
