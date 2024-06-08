import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Generate random training data
X_train = torch.tensor(np.random.rand(100, 3), dtype=torch.float32)
y_train = torch.tensor(np.sum(X_train.numpy(), axis=1), dtype=torch.float32)  # Sum of input features

# Define the neural network model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(3, 10)
        self.fc2 = nn.Linear(10, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Instantiate the model
model = SimpleModel()

# Define loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train the model
for epoch in range(50):
    optimizer.zero_grad()  # zero the gradient buffers
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()

# Save the trained model
torch.save(model.state_dict(), 'trained_model.pth')
