from typing import List, Sequence, Tuple

def verticesAsList(
        wp #: cq.Workplane
) -> List[Tuple[float,float]]:
    l: List[Tuple[float, float]] = []
    for i in wp.vertices().vals():
        l.append((i.X, i.Y))
    return l
