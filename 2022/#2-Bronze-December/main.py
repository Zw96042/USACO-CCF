"""
There are N cows lined up horizontally.

Each cow is willing to move a maximum of K 
positions to reach a patch.

There can be no patch, G patch, or a H patch. 
G cows need G grass and H cows need H grass. You cannot plant
both at the same location. Each patch can feed
unlimited # of cows of the appropriate breed.

Find the minimum # of patches
And then the configuration they sould be in

Cows don't have to move
"""
T = int(input())

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    patches = ['.'] * N
    last_g = -K - 1
    last_h = -K - 1
    S = input()

    count = 0

    for i in range(N):
        if S[i] == 'G' and i - last_g > K:
            last_g = min(i + K, N - 1)
            if patches[last_g] != ".":
                last_g -= 1
            patches[last_g] = "G"
            count += 1
        elif S[i] == 'H' and i - last_h > K:
            last_h = min(i + K, N - 1)
            if patches[last_h] != ".":
                last_h -= 1
            patches[last_h] = "H"
            count += 1

    print(count)
    print("".join(patches))
