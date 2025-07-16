"""Graph Neural Network model placeholder."""

import torch
from torch import nn
from torch_geometric.nn import GCNConv


class AccessibilityGNN(nn.Module):
    """Simple GNN architecture for accessibility scoring."""

    def __init__(self, in_channels: int, hidden_channels: int, out_channels: int):
        super().__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, out_channels)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index).relu()
        x = self.conv2(x, edge_index)
        return x


# Training utilities will be implemented here
