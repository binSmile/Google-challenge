# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solution(x):
    result = ''
    for i in x:
        n = ord(i)
        if (97 <= n <= 122):
            n = -n+219
        result += chr(n)
    return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))

"""Output:     did you see last night's episode?"""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
