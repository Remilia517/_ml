import torch

x = torch.tensor(0.0, requires_grad=True)
y = torch.tensor(0.0, requires_grad=True)
z = torch.tensor(0.0, requires_grad=True)

lr = 0.1
steps = 50

for step in range(steps):

    f = x**2 + y**2 + z**2 - 2*x - 4*y - 6*z + 8
    f.backward()

    with torch.no_grad():
        x -= lr * x.grad
        y -= lr * y.grad
        z -= lr * z.grad

        x.grad.zero_()
        y.grad.zero_()
        z.grad.zero_()

    print(f"Step {step+1}: x={x.item():.4f}, y={y.item():.4f}, z={z.item():.4f}, f={f.item():.4f}")
