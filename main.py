""" 
Problem Summary:
We have N cows of various heights in a line
who takes turns eating M candy canes. Every time a cow
eats a candy cane, they grow by the amount they ate.

Print final height for all cows
"""

N, M = [int(i) for i in input().split()]
cows = [int(i) for i in input().split()]
candy = [int(i) for i in input().split()]

# loop over candy canes
for i in range(M):
    candy_eaten = 0
    # loop over cows
    for j in range(N):
        # how much of the current candy cane is the current 
        # cow going to eat?
        cow_eats = min(candy[i], cows[j]) - candy_eaten
        if cow_eats <= 0:
            continue
        cows[j] += cow_eats
        candy_eaten += cow_eats

        if candy_eaten == candy[i]:
            break

for i in range(N):
    print(cows[i])