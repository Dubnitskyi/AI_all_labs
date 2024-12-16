def step_function(value):
    return 1 if value > 0 else 0

def perceptron_XOR(x1, x2):
    h1 = step_function(x1 - x2)
    h2 = step_function(x2 - x1)
    y = step_function(h1 + h2 - 0.5)
    return y

print("x1 x2 XOR")
for x1, x2 in [(0, 0), (0, 1), (1, 0), (1, 1)]:
    print(f"{x1}  {x2}   {perceptron_XOR(x1, x2)}")
