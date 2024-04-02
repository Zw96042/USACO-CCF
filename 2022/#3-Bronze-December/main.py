T = int(input())

def split(j, comp, out):
    # if (b[j] == comp) return out
    if (used[j]): 
        return False

    for i in range(M-1):
        if((len(strings[i]) != 0) and (strings[i][j] == comp) and (output[i] != out)):
            return False
        
    # Do split
    used[j] = True
    for i in range(M-1):
        if((len(strings[i]) != 0) and (strings[i][j] == comp)):
            strings[i] == ""
    return True

def all_equal(test_out):
    for i in range(M-1):
        if ((len(strings[i]) != 0) and (output[i] != test_out)):
            return False
    return True

for _ in range(T):
    line = input()
    N, M = (int(x) for x in input().split()) 
    strings = []
    output = []
    used = [""] * 100
    for _ in range(M):
        data = input().split()
        strings.append(data[0])
        output.append(data[1])

    for j in range(N-1):
        used[j] = False
    
    while True:
        split_found = False

        # Try splitting by each bit

        for j in range(N-1):
            if (
                split(j, "0", 0) or
                split(j, "0", 1) or
                split(j, "1", 0) or
                split(j, "1", 1)
            ):
                split_found = True

        if (not split_found):
            print("LIE")
            break
        if (all_equal(0) or all_equal(1)):
            print("OK")
            break