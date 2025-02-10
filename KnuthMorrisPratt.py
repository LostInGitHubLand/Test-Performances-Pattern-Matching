def compute_LPS(PATTERN):
    pre = 0
    lps = [0]*len(PATTERN)
    for i in range (1, len(PATTERN)):
        while(pre > 0 and PATTERN[i] != PATTERN[pre]):
            pre = lps[pre-1]
        if(PATTERN[pre] == PATTERN[i]):
            pre +=1
            lps[i]=pre
    return lps


def KMP_search(text, pattern):
    M = len(pattern)
    N = len(text)
    lps = compute_LPS(pattern)
    i = j = 0
    positions = []
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == M:
            positions.append(i - j)
            j = lps[j - 1]

        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return positions