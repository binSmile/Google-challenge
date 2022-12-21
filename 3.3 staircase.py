'''
The third level of tasks in google chalenge

With the LAMBCHOP doomsday device finished, Commander Lambda is preparing to debut on the galactic stage -- but in order to make a grand entrance, Lambda needs a grand staircase! As the Commander's personal assistant, you've been tasked with figuring out how to build the best staircase EVER.

Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so they can pick the one with the most options.

Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates a brick)

'''

# def briksSort(n):
#     if n <= 2:
#         return [n]
#     else:
#         stack = []
#         stack += [n]
#
#
#
#
# def solution(n):
#     stack = []
#     for i in range(n):
#         b = n-i
#         stack +=2
#
#     return
#


def solution(n):
    m = [[0 for i in range(n + 1)] for j in range(n + 1)]
    m[0][0] = 1  # base case
    for stair in range(1, n + 1):
        for left in range(0, n + 1):
            m[stair][left] = m[stair - 1][left]
            if left >= stair:
                m[stair][left] += m[stair - 1][left - stair]

    return m[n][n] - 1

print solutionA(9)

