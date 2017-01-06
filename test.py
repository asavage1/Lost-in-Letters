elements = [0, 1, 2] 
weights = [0.2, 0.3, 0.5]
result = [0] * 3
trials = 10000
expected = []

import random
for x in range(trials):
    result[random.choices(elements, weights)[0]] += 1
for each in weights:
    expected.append(int(each * trials))

print (expected)
print (result)
