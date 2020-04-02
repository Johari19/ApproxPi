import math
import random
# Monte Carlo Method
circle = 0
total = 5000000
radius = 100

# Main Loop
for i in range(0, total):

    # Random Coordinates
    x = random.uniform(-radius, radius)
    y = random.uniform(-radius, radius)

    # Distance
    distance = math.sqrt(x*x + y*y)
    if distance < radius:
        circle += 1
approxPi = 4 * (circle / total)
print(float(approxPi))
print(math.pi)
