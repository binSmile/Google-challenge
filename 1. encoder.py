# This is a sample Python script with first task from google

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

