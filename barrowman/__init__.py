# -*- coding: utf-8 -*-
from math import pi, atan, tan, radians

__author__ = 'Nathan Bergey'
__email__ = 'nathan.bergey@gmail.com'
__version__ = '0.0.1'


class Component(object):
    """Base class for a single rocket Component. This can be something
    like a nosecone or the body of a rocket. It is a physical thing that
    has a length and width, and therefore volume and area.
    """

    def __init__(self):
        return

    @property
    def length(self):
        """The length of the component"""
        return self._length

    @property
    def volume(self):
        """The volume of the component"""
        return self._volume()

    @property
    def area(self):
        """The area of the component"""
        return self._area()


class Nose(Component):
    """A Nosecone. Must be of a known shape (Conical, ogive, etc). The tip of
    the nose is assumed to be a sharp point and the datum (x=0) for all
    measurements.

    :param str shape: The type of nosecone, see class for list of valid shapes
    :param float width: The diameter of the nose [meters]
    :param float length: The length of the nose [meters]

    """

    CONE = 'cone'   #: Shape type 'cone'

    def __init__(self, shape, width, length):
        self.shape = shape
        self._width = width
        self._length = length
        self._radius = width / 2.0

    def _volume(self):
        if self.shape == self.CONE:
            return pi * self._radius**2 * self._length / 3.0
        return 0

    def _area(self):
        return pi * self._radius**2


class Tube(Component):
    """A cylindrical section of rocket.

    :param float width: The diameter of the section [meters]
    :param float length: The length of the section [meters]

    """

    def __init__(self, width, length):
        self._width = width
        self._length = length

    def _volume(self):
        return pi * (self._width/2.0)**2 * self._length

    def _area(self):
        return pi * self._radius**2


class Fin(Component):
    """A single trapezoidal fin.

    Note: though both sweep and sweepangle are optional, you probably need to specify at
    least one to correctly define a fin. Specifying both makes the system overdetermined.

    Nomenclature diagram:

    .. figure:: images/barrowman_fin_nomenclature.svg
       :alt: Diagram of Barrowman's fin nomenclature.

    :param float root: Length of the root chord of the fin [meters]
    :param float tip: Length of the tip chord of the fin  [meters]
    :param float span: Length of the span of the fin [meters]
    :param float sweep: (Optional, default=None) The length of the sweep portion [meters]
    :param float sweepangle: (Optional, default=45.0) The angle of the sweep [degrees]

    """

    def __init__(self, root, tip, span, sweep=None, sweepangle=45.0):
        self.root = root  #: Root Chord of fin
        self.tip = tip    #: Tip Chord of fin
        self.span = span  #: Span ("height") of fin
        self._length = root

        if sweep is not None:
            self.sweep = sweep  #: Sweep length of the fin
            self.sweepangle = atan(self.sweep / self.span)
            """Angle of sweep of the fin [radians]"""
        else:
            self.sweep = span * tan(radians(sweepangle))
            self.sweepangle = radians(sweepangle)
