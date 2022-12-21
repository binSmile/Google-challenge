
def solution(xs):
    xs_pos = []
    xs_neg = []
    xs_zer = []
    for x in xs:
        if x > 0:
            xs_pos += [x]
        elif x < 0:
            xs_neg += [x]
        else:
            xs_zer += [x]
    xs_neg.sort(reverse=True)
    F1, F2 = False, False
    powp, pown = 1,1
    if xs_pos:
        F1 = True
        for x in xs_pos:
               powp *= x
    if len(xs_neg) > 1:
        F2 = True
        if len(xs_neg) % 2 != 0:
            xs_neg.pop(0)
        for x in xs_neg:
            pown *= x

    if F1 or F2:
        return str(pown * powp)
    elif xs_neg and not xs_zer:
        return str(xs_neg[0])
    else:
        return '0'



testarrays = [[-2, -3, 4, -5],[2, -3, 1, 0, -5],[2, 0, 2, 2, 0]]

for s in testarrays:
    print(s)
    print(solution(s))
test = [1000*((-1)**num) for num in range(1,51)]
solution(test)