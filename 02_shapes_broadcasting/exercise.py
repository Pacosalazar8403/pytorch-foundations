import torch

#1. Create torch.rand(4, 1, 28, 28) (4 grayscale images). Flatten each image so the shape is [4, 784]. Use view with -1.
img = torch.rand(4, 1, 28, 28)
flat = img.view(4, -1)
print(flat.shape)

#2. Without running it, predict the shape of torch.rand(5, 1) + torch.rand(1, 7). Then run it.
a = torch.rand(5, 1)
b = torch.rand(1, 7)
print((a + b).shape)

#3. You have x of shape [64, 512] and want 10 outputs. What shape must W be? Make it and verify.
x = torch.rand(64, 512)
W = torch.rand(512, 10)

result = x @ W

print(W.shape)
print(result.shape)