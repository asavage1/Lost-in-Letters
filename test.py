elements = ['one', 'two', 'three'] 
p = [0.2, 0.3, 0.5]

import random
#print (random.choice(elements))
print (random.choices(elements, weights = p))
