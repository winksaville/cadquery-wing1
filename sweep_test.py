a = 1
b = 5
h = b*5
d = a*5

s = (
    cq.Workplane("XY")
    .ellipse(a,b)
    .sweep(
        cq.Workplane("XZ")
        .spline([(0,0),(0,h),(d,h+5*d)],[(0,1),(1,1)])
    )
)
