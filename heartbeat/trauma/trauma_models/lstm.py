import torch.nn as nn

class LSTM(nn.Module):
  def __init__(self, input_dim, hidden_dim, output_dim):
    super().__init__()
    self.hidden_dim = hidden_dim
    self.lstm = nn.LSTM(input_dim, hidden_dim)
    self.fc = nn.Linear(hidden_dim, output_dim)
    self.softmax = nn.LogSoftmax(dim=1)

  def forward(self, x):
    lstm_out, (h_n, c_n) = self.lstm(x)
    output = self.fc(lstm_out)
    output = self.softmax(output)
    return output