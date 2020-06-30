# The rotate is being disregard.
# See:
#    https://groups.google.com/g/cadquery/c/swIm32rwbKg/m/E0p_ONahAwAJ

#el = (
#    cq.Workplane("XY")
#    .ellipse(1, 5)
#    .rotate(
#        axisStartPoint=(0, 0, 0),
#        axisEndPoint=(0, 0, 1),
#        angleDegrees=90)
#)

# Jeremey in post:
#    https://groups.google.com/g/cadquery/c/swIm32rwbKg/m/-sSXcpvnAwAJ
# suggests using transformed instead, this "works".
oel = (
    cq.Workplane("XY")
    .ellipse(1, 5)
)

el = (
    cq.Workplane("XY")
    .transformed(rotate=(0, 0, 90))
    .ellipse(1, 5)
)

r = el.extrude(25)
