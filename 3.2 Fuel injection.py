'''
The third level of tasks in google chalenge

Add one fuel
rem one fuel
Div by 2 (even pellets)

309 digits long
minimum transform operation to 1

solution(4) returns 2: 4 -> 2 -> 1
solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

111 > 112 > 56 -> 28 -> 14 > 7 > 8 > 4 > 2


'''
# 100 > 50 > 25 > 24 > 12 > 6 > 3 > 2 > 1
# 100 > 50 > 25 > 24 > 12 > 6 > 3 > 4 > 2
def solution(n):
    n = long(n)
    c = 0
    while n > 1:
        bb = bin(n)
        c += 1
        if n % 2 == 0:
            n /= 2
        else:
            if bin(n)[-2:-1] == '1' and n != 3:
                n += 1
            else:
                n -= 1
    return c


def solution_stupid(n):
    n = long(n)
    if n == 1:
        A = 0
    elif n == 2:
        A = 1
    elif n % 2 == 0:
        A = 1 + solution_stupid(n / 2)
        # print(n,'div2')
    else:
        v1 = solution_stupid((n - 1) / 2)
        v2 = solution_stupid((n + 1) / 2)
        if v1 < v2:
            o = '-'
        elif v2 < v1:
            o = '+'
        else:
            o = '='
        # print(n,o,v1,v2,bin(n))
        A = 2 + min(v1,v2)

    return A


import sys
sys.setrecursionlimit(3333)
def solution_ss(n):
    n = int(n)
    if n <= 2:
        return n - 1
    if n % 2 == 0:
        return solution_ss(n // 2) + 1
    return min(solution_ss(n + 1), solution_ss(n - 1)) + 1

def stepCount(n):
	count = 0
	while n > 1:
		if n % 2 == 0:             # bitmask: *0
			n = n // 2
		elif n == 3 or n % 4 == 1: # bitmask: 01
			n = n - 1
		else:
			n = n + 1              # bitmask: 11
		count += 1
	return count

# print solution(100)
# print stepCount(100)
print(solution(str(10**309 - 1)))
for i in range(100,150):
    my = solution(i)
    check = stepCount(i)
    if my != check:
        print(i,my, check)
