'''
The 4th level of tasks in google chalenge
'''

def solution(M, F,first=True):
    M, F = long(M),long(F)
    if (M > 1 and F > 1):
        if M != F:
            M, F = min(M, F), max(M, F)
            magic = F - M * (F / M)
            if magic:
                sol = solution(M, magic, first=False)
                if sol == 'impossible':
                    return 'impossible'
                A = sol + (F / M) - 1
            else:
                return 'impossible'
        else:
            return 'impossible'
    elif M == F and M == 1:
        return 0
    elif M == 1 or F == 1:
        A = max(M, F) - 1

    if first:
        return str(A)
    else:
        return A + 1

#
# def solutionO(M, F,first=True):
#     M, F = long(M),long(F)
#     if (M > 1 and F > 1):
#         if M != F:
#             M, F = min(M,F), max(M,F)
#             if M != 1:
#                 A = solution(M, F - M * (F / M), first=False)+(F/M)-1
#             else:
#                 return F/M-1
#
#         else:
#             return 'impossible'
#         if A == 'impossible':
#             return 'impossible'
#         else:
#             if first:
#                 return str(A-1)
#             else:
#                 return A+1
#     if M == F == 1:
#         return 0
#     elif M == 1 or F == 1:
#         return F / M - 2
#     else:
#         return 'impossible'



# print(solution('4', '7'))  # 4
# print(solution('2', '1'))  # 1
# print(solution('2', '4'))  # impossible

import random
m = random.randint(2,1e50)
f = random.randint(2,1e50)
print solution(m,f)