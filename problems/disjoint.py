m = [1, 2, 3]
n = [4, 5, 3]

def disjoint(set1, set2):
    for a in set1:
        for b in set2:
            if a is b:
                return 0
    return 1

def disjoint_sorted(set1, set2):
    for a in set1:
        for b in set2:
            if a is b:
                return 0
    return 1

print(disjoint(m, n))
