k = int(input("How many Fibonacci numbers would you like to generate? "))
seq = []
a, b = 0, 1
while len(seq) < k:
    seq.append(a)
    a, b = b, a + b
print("The Fibonacci Sequence is:", ", ".join(map(str, seq)))