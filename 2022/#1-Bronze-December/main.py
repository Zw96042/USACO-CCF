N = int(input())
C = [int(i) for i in input().split()]

revenue = min(C)
tuition = 1000000

C.sort()

for i in range(N-1):
    revenue = max((N - i) * C[i], revenue)
    
for i in range(N-1):
    if revenue == (N - i) * C[i]:
        tuition = min(C[i], tuition)
    
print(revenue, tuition)