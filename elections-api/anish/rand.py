import random
Signal = ['Stop', 'Wait', 'Go']
for K in range(2, 0, -1):
    R = random.randrange(K)
    print(Signal[R], end='#')

print()
print(random.randrange(7))
print(random.randrange(2))
print(random.randrange(1))

for i in range(2, 0, -1):
    print(i)