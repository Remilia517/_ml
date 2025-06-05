import torch
import torch.nn as nn
import matplotlib.pyplot as plt

x = torch.tensor([0, 1, 2, 3, 4], dtype=torch.float32).view(-1, 1)
y = torch.tensor([1.9, 3.1, 3.9, 5.0, 6.2], dtype=torch.float32).view(-1, 1)

model = nn.Linear(in_features=1, out_features=1)

loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

epochs = 3000
for epoch in range(epochs):
    y_pred = model(x)

    loss = loss_fn(y_pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 500 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

params = list(model.parameters())
print(f"Learned parameters: w = {params[0].item():.4f}, b = {params[1].item():.4f}")

predicted = model(x).detach().numpy()
plt.plot(x.numpy(), y.numpy(), 'ro', label='Original data')
plt.plot(x.numpy(), predicted, label='Fitted line')
plt.legend()
plt.show()
