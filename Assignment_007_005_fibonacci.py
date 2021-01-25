fibonacci = [1, 1]
for i in range(0,55):
    if 55 not in fibonacci:
        fibonacci.append(fibonacci[i+1]+fibonacci[i])
print(fibonacci) 