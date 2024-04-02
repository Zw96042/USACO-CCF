S = [int(i) for i in input().split()]

ABC = max(S) 
S.remove(ABC)

A = min(S) 
S.remove(A)

B = min(S) 
S.remove(B)

C = ABC - A - B

print(A, B, C)