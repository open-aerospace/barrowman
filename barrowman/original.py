"""
The Barrowman Method
====================

A python implementation of the original `Barrowman Method`_ for the approximate
evaluation of the aerodynamic model of a rocket.

.. _Barrowman Method: http://ntrs.nasa.gov/search.jsp?R=20010047838

From the paper:

    STATEMENT OF PROBLEM

    Determine a set of expressions for the practical calculation of
    the aerodynamic characteristics of slender, axisymmetric finned
    vehicles at both subsonic and supersonic speeds. The
    characteristics of interest are the normal force coefficient
    derivative, C_Na; center of pressure, Xbar; roll forcing moment
    coefficient derivative, C_ls; roll damping moment coefficient
    derivative, C_lp; pitch damping moment coefficient derivative,
    C_mq; and drag coefficient, C_D.


    GENERAL METHOD OF SOLUTION

    1. Divide vehicle into body and tail.
    2. Analyze the body and tail separately. Subdivide either when necessary
    3. Analyze wing-body interference.
    4. Recombine to form total vehicle solution.


    GENERAL ASSUMPTIONS

    1. The angle-of-attack is very near zero.
    2. The flow is steady and irrotational.
    3. The vehicle is a rigid body.
    4. The nose tip is a sharp point.

"""
# -*- coding: utf-8 -*-


class Body(object):
    """Aerodynamic model of the body section (excluding fins) of a rocket

    :param list body: A list of body components (Nose, tube, transition, etc.)

    Members:
    """

    def __init__(self, body):
        length = 0
        volume = 0
        for component in body:
            length += component.length
            volume += component.volume

        self.l_0 = length
        self.V_B = volume
        self.A_B = body[0].area

    def C_P(self):
        """Center of Pressure.

        :returns: the center of pressure of the rocket body in meters (tip of nose = 0)

        """

        """According to the paper, the center of pressure of a cylindrical
        body can be simplified to:

            X = l_0 - [V / A]       (eq. 3-89, pg. 29)

        where:
         - X:   Longitudinal center of pressure
         - l_0: Body Length
         - V: Body Volume
         - A: Base Area
        """

        return self.l_0 - (self.V_B/self.A_B)
