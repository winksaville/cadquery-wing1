from mh49 import mh49
from scale import scaleListOfTuple
from fattenTe import fattenTe
from dumpAttr import dumpAttr
from verticesAsList import verticesAsList

from pprint import pprint
import cadquery as cq # type: ignore

from typing import List, Sequence, Tuple

chord: float = 50
span: float = 20
tip: float = 5

# Normalize, Scale, fattenTe
scaleFactor: float = 1/mh49[0][0]
nMh49 = scaleListOfTuple(mh49, scaleFactor)
sMh49: List[Tuple[float, float]] = scaleListOfTuple(nMh49, chord)
fMh49: List[Tuple[float, float]] = fattenTe(sMh49, 0.5, 10)

h = 100
d = 25

# Use "XY" with Jeremey's transformed(rotate) technique
result = (
    cq.Workplane("YX")
    .polyline(fMh49).close()
    #.spline(fMh49).close()
    .transformed(rotate=(0, 0, 90))
    .sweep(
        cq.Workplane("XZ")
        # Start 0deg tangent, Tip finishes with 90deg tangent
        .spline([(0, i) for i in range(h-10)] + [(d-5,h+10)],[(0,1),(1,0)])

        # Start 0deg tangent, Tip finishes with 45deg tangent
        #.spline([(0,0),(0,h),(d,h+(5*d))],[(0,1),(1,1)]) #original
    )
)

#pprint(vars(result))
import io
tolerance=0.1;
f = io.open(f'wing1-vtips-loose-direct-{tolerance}.stl', 'w+')
cq.exporters.exportShape(result, cq.exporters.ExportTypes.STL, f, tolerance)
f.close()

