import sys
log(f'sys.path={sys.path}')

from mh49 import mh49
from scale import scaleListOfTuple
from fattenTe import fattenTe
#from pprint import pprint
import cadquery as cq # type: ignore

from typing import Tuple, List

chord: float = 50
span: float = 20

# Normalize mh49 to 1. Assumes first point is
# the length of the chord and will scale all
# of the points to 1/mh49[0][0]
scaleFactor: float = 1/mh49[0][0]
#print(f'scaleFactor={scaleFactor}')
nMh49 = scaleListOfTuple(mh49, scaleFactor)

# Scale the normalized mh49 to the size of the chord
# and turn it into a list
sMh49: List[Tuple[float, float]] = scaleListOfTuple(nMh49, chord)
#print(f'SKINNY   sMh49={sMh49}')
fMh49: List[Tuple[float, float]] = fattenTe(sMh49, 0.5, 10)
#print(f'FATTENed fMh49={fMh49}')

result = cq.Workplane("XY").spline(fMh49).close().extrude(span)
#pprint(vars(result))
import io
tolerance=0.001;
f = io.open(f'wing1-spline-50x20-direct-{tolerance}.stl', 'w+')
cq.exporters.exportShape(result, cq.exporters.ExportTypes.STL, f, tolerance)
f.close()
