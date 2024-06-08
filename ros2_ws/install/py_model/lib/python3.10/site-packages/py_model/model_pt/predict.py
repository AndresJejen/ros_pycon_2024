import torch
import numpy as np
import torch.nn as nn

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

# Load the trained model state
model.load_state_dict(torch.load('/root/ros/demo_code/ros2_ws/src/py_model/py_model/model_pt/trained_model.pth'))

# Function to make predictions
def predict(inputs):
    inputs = torch.tensor(inputs, dtype=torch.float32).unsqueeze(0)  # Reshape inputs as model expects
    prediction = model(inputs)
    return prediction.item()

# Example usage
if __name__ == "__main__":
    inputs = [0.1, 0.2, 0.3]
    output = predict(inputs)
    print("Prediction:", output)
