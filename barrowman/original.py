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


class Rocket(object):
    """Full solution for a rocket"""

    def __init__(self, body, tail):
        self.body = body
        self.tail = tail

    def C_P(self, Mach):
        return self.body.C_P(Mach) + self.tail.C_P(Mach)


class Body(object):
    """Aerodynamic model of the body section (excluding fins) of a rocket. This includes
    the nose cone.

    Nomenclature diagram:

    .. figure:: images/barrowman_nomenclature.svg
       :alt: Diagram of Barrowman's rocket parts nomenclature.

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

    def C_P(self, Mach):
        """Center of Pressure.

        :param float Mach: Mach number of the air-stream over the rocket [dimensionless]
        :returns: the center of pressure of the rocket body in [meters] (tip of nose = 0)

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


class Tail(object):
    """The tail section of the rocket: i.e. the part with fins. Assume that
    each fin is exactly the same and evenly spaced, and the bottom of the root
    chord is also the bottom of the rocket.

    Nomenclature diagram:

    .. figure:: images/barrowman_nomenclature.svg
       :alt: Diagram of Barrowman's rocket parts nomenclature.

    Takes a fin definition and the number of fins.

    :param Fin fin: A Fin object
    :param int N: The number of fins on the tail
    """

    def __init__(self, fin, N):
        self._fin = fin

    def C_P(self, Mach):
        """Center of Pressure.

        :param float Mach: Mach number of the air-stream over the rocket [dimensionless]
        :returns: the center of pressure of the rocket body in [meters] (tip of nose = 0)

        """

        """Subsonic C_P is assumed to be the intersection of the 1/4 chord, and
        the mean aerodynamic chord. "After much algebra" the paper says:

        X = l_T + (x_t/3)[(c_r + 2c_t)/(c_r + c_t)] + 1/6[c_r + c_t  - (c_r * c_t)/(c_r + c_t)]

        (eq. 3-10, pg. 10)

        where:
         - l_T = X coord of beginning of the fin (X=0 is tip of the nosecone)
         - x_t = Sweep of fin === Fin Span*tan(sweepangle)
         - c_r = Root Chord of fin
         - c_t = Tip Chord of fin

        In this case we want to return the partial X, so we ignore l_T (we don't know it yet anyway)
        """

        x_t = self._fin.sweep
        c_r = self._fin.root
        c_t = self._fin.tip

        X = ((x_t / 3.0) * ((c_r + (2 * c_t)) / (c_r + c_t)))
        X += (1 / 6.0) * (c_r + c_t  - (c_r * c_t)/(c_r + c_t))

        return X
