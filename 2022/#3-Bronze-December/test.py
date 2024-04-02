def solve():
    nvars, ninputs = (int(x) for x in input().split())
    inputs = []
    results = []
    for _ in range(ninputs):
        data = input().split()
        inputs.append(data[0])
        results.append(data[1])
    programs = [i for i in range(ninputs)]
    while True:
        updated = False
        for i in range(nvars):
            if updated:
                break
            offvals = set()
            offinputs = []
            onvals = set()
            oninputs = []
            for j in programs:
                if inputs[j][i] == '1':
                    onvals.add(results[j])
                    oninputs.append(j)
                else:
                    offvals.add(results[j])
                    offinputs.append(j)
            if len(offvals) <= 1 and len(onvals) <= 1:
                print("OK")
                return
            if len(offvals) == 0 or len(onvals) == 0:
                continue
            if len(offvals) == 2 and len(onvals) == 2:
                continue
            if len(offvals) == 1:
                updated = True
                programs = oninputs
            elif len(onvals) == 1:
                updated = True
                programs = offinputs
            else:
                assert False
        if not updated:
            print("LIE")
            return
 
t = int(input())
for _ in range(t):
    input()
    solve()