import torch 

a = torch.tensor([1, 2, 3])
b = torch.tensor([[1, 2], [3, 4]])
print(a.dtype, b.dtype)
print(b.shape, b.ndim)
print(b.float().mean())


z = torch.zeros(2, 3) # Creates a 2 × 3 tensor filled with zeros
o = torch.ones(2, 3) # Creates a 2 × 3 tensor filled with ones
r = torch.rand(2, 3) #Creates a 2 × 3 tensor filled with random numbers from 0-1.
ar = torch.arange(0, 10, 2)

print(b[0]) #prints the first row of the matrix
print(b[1]) #prints the second row of the matrix
print(b[:, 0]) #prints the first column of the matrix
print(b[:, 1]) #prints the second column of the matrix
print(b[1, 0]) # row 2, column 1: 3.0, turn tensor into a python number

print(a + 10) 
print(a * a)
print(b @ b) # Creates a 2 × 3 tensor filled with zeros

