def fibonacci_seq(n):
    if(n == 0):
      return 0
    elif(n == 1):
      return 1
    else:
     return (fibonacci_seq(n - 2) + fibonacci_seq(n - 1))
n = int(input("Enter the number:  "))
print("Fibonacci Sequence is:", end = ' ')
for n in range(0, n):
    print(fibonacci_seq(n), end = ' ')
