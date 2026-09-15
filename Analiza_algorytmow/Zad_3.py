n = 10

P = [0] * (n + 1)
S = [0] * (n + 1)

for i in range(1, n + 1):
    P[i] = 1
    S[i] = 0
for j in range(2, n + 1):
    if P[j] == 1:
        i = j * j
        while i <= n:
            P[i] = 0
            i = i + j
    S[j] = S[j - 1] + P[j]

print(P[1:])
print(S[1:])