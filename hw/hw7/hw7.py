from micrograd.engine import Value

def optimize_with_micrograd(lr=0.1, steps=50):
    x = Value(0.0)
    y = Value(0.0)
    z = Value(0.0)

    for step in range(steps):
        f = x**2 + y**2 + z**2 - 2*x - 4*y - 6*z + 8

        x.grad = 0
        y.grad = 0
        z.grad = 0

        f.backward()

        x.data -= lr * x.grad
        y.data -= lr * y.grad
        z.data -= lr * z.grad

        print(f"Step {step+1}: x={x.data:.4f}, y={y.data:.4f}, z={z.data:.4f}, f={f.data:.4f}")

    return x, y, z, f

if __name__ == '__main__':
    optimize_with_micrograd()
