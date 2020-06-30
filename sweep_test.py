a = 1
b = 5
h = b*5
d = a*5

s = (
    cq.Workplane("XY")
    .ellipse(a,b)
    .sweep(
        cq.Workplane("XZ")
        # Start 0deg tangent, Tip finishes with 90deg tangent
        .spline([(0, i) for i in range(h)] + [(d,h)],[(0,1),(1,0)])

        # Start 0deg tangent, Tip finishes with 45deg tangent
        #.spline([(0,0),(0,h),(d,h+5*d)],[(0,1),(1,1)]) #original
    )
)
