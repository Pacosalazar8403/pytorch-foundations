import torch 

#1. Make a 5 x 5 tensor of random numbers. Print the value in row 3, column 2 as a plain Python float.
x = torch.tensor(5, 5)
print(2, 1).item()

#2. Make torch.arange(1, 11) and get only the even numbers using a boolean mask (t[t % 2 == 0]).
t = torch.arange(1, 11)
print(t[t % 2 == 0])

#3. Create two 3 x 3 tensors. Compute their element-wise product and their matrix product. Explain in one sentence why they differ.
a = torch.tensor([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

b = torch.tensor([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(a * b)
print(a @ b)
#Element-wise product is the multiplication of corresponding elements in the 2 tensors, while the matrix product calculates dot product between rows and columns.