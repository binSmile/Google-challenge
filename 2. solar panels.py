
def solution(xs):
    import numpy as np
    a = np.array(xs)

    cond1 = (a > 0)
    pow1 = a[cond1].prod()

    cond2 = (a < 0)
    xsc2 = a[cond2]
    pow2 = 1
    if len(xsc2) > 1:
        if len(xsc2) % 2 == 0:
            pow2 = xsc2.prod()
        else:
            maxx = xsc2.argmax()
            pow2 = np.delete(xsc2, maxx).prod()
    return pow1*pow2

testarrays = [[-2, -3, 4, -5],[2, -3, 1, 0, -5],[2, 0, 2, 2, 0]]
for s in testarrays:
    print(s)
    print(solution(s))