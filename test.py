import random

def listsum(weights):
    sum = 0
    for i in weights:
        sum += i
    return sum

def dothis():
    elements = [0, 1, 2] 
    weights = [0.2, 0.3, 0.6]
    result = [0] * 3
    trials = 100000
    expected = []
    diff = []

    for x in range(trials):
        result[random.choices(elements, weights)[0]] += 1
            
    for each in weights:
        expected.append(int(each * trials / listsum(weights)))
            
    for i in range(len(weights)):
        diff.append(abs(expected[i] - result[i]))
            
    print (diff)

for x in range(10):
    dothis()
