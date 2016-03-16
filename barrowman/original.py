"""
The Barrowman Method
====================

A python implementation of the original `Barrowman Method`_ for the approximate
evaluation of the aerodynamic model of a rocket.

.. _Barrowman Method: http://ntrs.nasa.gov/search.jsp?R=20010047838

Classes:
--------

"""
# -*- coding: utf-8 -*-


class Body(object):
    """Aerodynamic model of a cylindrical rocket body

    :param float diameter: The diameter of the rocket body
    :param float length: The length of the rocket body

    Members:
    """

    def __init__(self, diameter, length):
        self.d = diameter
        self.l = diameter

    def C_P(self):
        """Center of Pressure.

        :returns: the center of pressure of the rocket body (float)

        """

        return 0.8
