from verticesAsList import verticesAsList

orgRect = (
    cq.Workplane("XY")
    .rect(1, 5)
)

rotRect = (orgRect
    .rotate(
        axisStartPoint=(0, 0, 0),
        axisEndPoint=(0, 0, 1),
        angleDegrees=90)
)

rectVertices = verticesAsList(rotRect);
print(f'rectVertices={rectVertices}')

srv = (
    cq.Workplane("XY")
    .polyline(rectVertices).close()
)

r = srv.extrude(25)
