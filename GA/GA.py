import random
import matplotlib.pyplot as plt
import numpy as np

def foo(x,y): #beale function f(3,0.5)=0
    return pow(1.5 - x +  x*y,2)+pow(2.25-x+ x*pow(y,2),2)+pow(2.625-x+ x* pow(y,3),2)

def fitness(x,y):
    ans = foo(x,y)
    return abs(1/ans)

def crossover(bestSolutions):
    for s in bestSolutions:
        elements.append(s[1][0])
        elements.append(s[1][1])
    return elements

def mutation(elements):
    for _ in range(1000):
        el = random.choice(elements) * random.uniform(0.99,1.01)
        e2 = random.choice(elements) * random.uniform(0.99,1.01)
        newGen.append((el,e2))
    return newGen

solutions = []
for s in range(1000):
    solutions.append( (random.uniform(0,1000), random.uniform(0,1000)))

for i in range(10000):
    rankedSolutions = []
    for s in solutions:
        rankedSolutions.append((fitness(s[0], s[1]), s))
        rankedSolutions.sort(reverse=True)
    print(f"Generacja {i}: {rankedSolutions[0]}")

    if rankedSolutions[0][0] > 9999:
        break
    bestSolutions = rankedSolutions[:100]
    elements = []
    crossover(bestSolutions)
    newGen = []
    mutation(elements)
    solutions = newGen


x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = foo(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)

ax.scatter(rankedSolutions[0][1][0], rankedSolutions[0][1][1], 0,c='r', marker='x')

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.title("Beale function")
plt.show()