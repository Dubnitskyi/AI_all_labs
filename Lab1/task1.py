def OR(x1, x2):
    return x1 or x2

def AND(x1, x2):
    return x1 and x2

def XOR(x1, x2):
    return OR(x1, x2) and not AND(x1, x2)

inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
print("x1 x2 XOR")
for x1, x2 in inputs:
    print(f"{x1}  {x2}   {XOR(x1, x2)}")
