from mh49 import mh49
from scale import scaleListOfTuple
from pprint import pprint
import cadquery as cq


chord: float = 50
span: float = 50

# Normalize mh49 to 1. Assumes first point is
# the length of the chord and will scale all
# of the points to 1/mh49[0][0]
scaleFactor = 1/mh49[0][0]
print(f'scaleFactor={scaleFactor}')
nMh49 = scaleListOfTuple(mh49, scaleFactor)

# Scale the normalized mh49 to the size of the chord
# and turn it into a list
sMh49 = scaleListOfTuple(nMh49, chord)
#print(f'sMh49={sMh49}')

result = cq.Workplane("XY").polyline(sMh49).close().extrude(span)
pprint(vars(result))
#show_object(result)
