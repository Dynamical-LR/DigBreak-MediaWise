import torch
from torch import nn


class SalesLSTM(nn.Module):
    def __init__(self, params_list: int):
        super().__init__()
        self.lstm = nn.LSTM(input_size=params_list, hidden_size=50, num_layers=4, batch_first=True)

        self.linear1 = nn.Linear(50, 100)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(100, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x, _ = self.lstm(x)
        x = x[:, -1, :]
        x = self.relu(self.linear1(x))
        return self.linear2(x)