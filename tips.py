from mh49 import mh49
from naca0009 import naca0009
from scale import scaleListOfTuple
from fattenTe import fattenTe
import cadquery as cq # type: ignore

from typing import Tuple, List

chord: float = 50
span: float = 150

# Normalize mh49, scale to chord and then fatten trailing edge
scaleFactor: float = 1/mh49[0][0]
nMh49 = scaleListOfTuple(mh49, scaleFactor)
sMh49: List[Tuple[float, float]] = scaleListOfTuple(nMh49, chord)
fMh49: List[Tuple[float, float]] = fattenTe(sMh49, 0.5, 10)
#result = cq.Workplane("XY").spline(fMh49).close().extrude(span)

# Normalize naca0009, scale to chord and then fatten trailing edge
scaleFactor = 1/naca0009[0][0]
nNaca0009 = scaleListOfTuple(naca0009, scaleFactor)
sNaca0009: List[Tuple[float, float]] = scaleListOfTuple(nNaca0009, chord)
fNaca0009: List[Tuple[float, float]] = fattenTe(sNaca0009, 0.5, 10)
#result = cq.Workplane("XY").spline(fNaca0009).close().extrude(span)

# For some reason second spline is shifted
#result = (cq.Workplane("XY")
#    .spline(fMh49).close()
#    .workplane(offset=span * 0.5)
#    .center(x=-chord/2.0, y=0) # Correct for shift (not exactly chord/2.0!)
#    .circle(5) #.spline(fMh49).close()
#    #.workplane(offset=span * 0.25)
#    #.center(x=-chord/2.0, y=0) # Correct for shift (not exactly chord/2.0!)
#    #.spline(fNaca0009).close()
#    .loft()
#)

rootWing = (cq.Workplane("XY", origin=(0, 0, 0))
    .spline(fMh49).close()
    .extrude(span * 0.95)
)

# Tip needs to bend approx. 90degs maybe make this
# a separate part, the "bend or joint"
tip = (cq.Workplane("XY", origin=(0, 0, span * 0.98)) # leave a slight gap for now
    .spline(fMh49).close()
    .workplane(offset=span * 0.20)
    .center(x=-chord/2.0, y=0) # Correct for shift WHY. and why not exactly chord/2.0!
    .spline(fNaca0009).close()
    .loft()
)

# When viewed as wireframe we see a "double" image.
# So I don't seem to be doing this correctly
#wing = rootWing.union(tip)
