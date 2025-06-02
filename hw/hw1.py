import random

def hillClimbing(f, x, y, z, h=0.01):
    failCount = 0
    while failCount < 10000:
        fxyz = f(x, y, z)
        dx = random.uniform(-h, h)
        dy = random.uniform(-h, h)
        dz = random.uniform(-h, h)

        if f(x + dx, y + dy, z + dz) < fxyz:
            x = x + dx
            y = y + dy
            z = z + dz
            print('x={:.3f} y={:.3f} z={:.3f} f(x,y,z)={:.3f}'.format(x, y, z, fxyz))
            failCount = 0
        else:
            failCount = failCount + 1

    return (x, y, z, fxyz)

def f(x, y, z):
    return x*x + y*y + z*z - 2*x - 4*y - 6*z + 8

hillClimbing(f, 0, 0, 0)
