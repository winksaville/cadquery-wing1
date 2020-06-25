from mh49 import mh49
from scale import scaleTuple, scaleTupleZ, scaleListOfTuple
import cadquery as cq

#afPts = [(1, 0), (0.25, 0.075), (0, 0), (0.35, 0.025)]
#print(f'afPts={afPts}')

chord: float = 50
span: float = 50

#def scaleTupleX(t, v):
#    """Scale the elements of the tuple by v"""
#    print(f'scaleTupleX: t={t} v={v}')
#    return tuple(map(lambda p: p * v, t))

#def scaleTuple(t, v):
#    """Scale the elements of the tuple by v"""
#    return tuple(map(lambda p: p * v, t))

# Normalize mh49 to 1. Assumes first point is the length of the chord
# and will scale it to 1
scaleFactor = 1/mh49[0][0]
print(f'scaleFactor={scaleFactor}')
#nMh49 = map(lambda t: scaleTupleX(t, scaleFactor), mh49)
nMh49 = scaleListOfTuple(mh49, scaleFactor)

# Scale the normalized mh49 to the size of the chord
# and turn it into a list
#sMh49 = list(map(lambda t: scaleTuple(t, chord), nMh49))
sMh49 = scaleListOfTuple(nMh49, chord)
print(f'sMh49={sMh49}')

result = cq.Workplane("XY").polyline(sMh49).close().extrude(span)
show_object(result)
