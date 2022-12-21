import sys


def solution(L): # L contain digits from 0 to 9
    L.sort(reverse=True)
    if not L:
        return 0

    def conclude(Ls):
        line = ''
        for ll in Ls:
            line += str(ll)
        return int(line)

    def checkContinue(num):
        return len(str(num)) > 1 \
               or (num % 3 == 0)


    num = conclude(L)
    while checkContinue(num):
        if num % 3 == 0:
            return num
        else:
            mod3 = num % 3
            modl = {1:[],2:[]}
            for i in L[::-1]:
                m = int(i) % 3
                if m != 0:
                    modl[m] += [i]

            if mod3 == 1:
                if modl[1]:
                    L.remove(modl[1][0])
                else:
                    if modl[2]:
                        L.remove(modl[2][0])
                    else:
                        return 0
            elif mod3 == 2:
                if modl[2]:
                    L.remove(modl[2][0])
                else:
                    if modl[1]:
                        if len(modl[1]) >= 2:
                            L.remove(modl[1][0])
                            L.remove(modl[1][1])
                            if not L:
                                return 0
                        else:
                            return 0
        num = conclude(L)
    return 0

from collections import deque

from itertools import combinations
import itertools
itertools.combinations()
def answer(l):
	l.sort(reverse = True)
	for i in reversed(range(1, len(l) + 1)):
		for tup in combinations(l, i):
			if sum(tup) % 3 == 0: return int(''.join(map(str, tup)))
	return 0

if __name__ == '__main__':
    # for i in range(99999,999999):
    #
    #     todo = map(int,list(str(i)))
        s2 = answer([3,5,4,8,9,1])
    #     s1 = solution(todo)
    #     if s1 != s2:
    #         print 'Attention' + str(i)
    #         sys.exit(1)
    # print 'well done'


# 4311
# 94311