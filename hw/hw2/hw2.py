import random

citys = [ 
    (0, 3), (0, 0),
    (0, 2), (0, 1),
    (1, 0), (1, 3),
    (2, 0), (2, 3),
    (3, 0), (3, 3),
    (3, 1), (3, 2)
]

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def pathLength(path):
    dist = 0
    for i in range(len(path)):
        dist += distance(citys[path[i]], citys[path[(i+1) % len(path)]])
    return dist

def getNeighbor(path):
    new_path = path[:]
    i, j = random.sample(range(len(path)), 2)
    new_path[i], new_path[j] = new_path[j], new_path[i]
    return new_path

def hillClimb(iterations=10000):

    current_path = list(range(len(citys)))
    random.shuffle(current_path)
    current_length = pathLength(current_path)

    print(f"初始路徑長度: {current_length:.3f}, 路徑: {current_path}")

    for _ in range(iterations):
        neighbor = getNeighbor(current_path)
        neighbor_length = pathLength(neighbor)

        if neighbor_length < current_length:
            current_path = neighbor
            current_length = neighbor_length
            print(f"   {current_length:.3f}  {current_path}")

    return current_path, current_length

best_path, best_length = hillClimb()
print("pathLength= ", best_length, best_path)
