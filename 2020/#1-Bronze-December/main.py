S = [int(i) for i in input().split()]

ABC = max(S) # The sum of A, B, and C will always be the highest integer

A = min(S) # A is ALWAYS the least inclusive value
S.remove(A) # Remove A to find a different minimum aside from A

B = min(S) # B is ALWAYS the 2nd lowest value aside from A

C = ABC - A - B # Calculate C using sum of ABC, A, and B

print(A, B, C) # Print in correct format