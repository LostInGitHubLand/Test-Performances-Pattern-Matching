def bruteForce (p, t):
    occurrences = []
    for i in range(len(t)-len(p)+ 1):
        match = True
        for j in range (len(p)):
            if t[i+j] != p[j]:
                match = False
                break
        if match: 
            occurrences.append(i)
    return occurrences