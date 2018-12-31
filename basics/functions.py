def fibonacci(depth):
    if (depth == 0):
        return 0;
    elif (depth == 1):
        return 1;
    else:
        return fibonacci(depth - 2) + fibonacci(depth - 1)

for index in range(0, 10):
    print(fibonacci(index))
