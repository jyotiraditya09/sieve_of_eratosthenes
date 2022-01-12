x = int(input("Enter a num till where you want to find a prime number: "))
primes = [i for i in range(2, x + 1)]
for i in range(2, x + 1):
    for j in primes:
        if i != j:
            if j % i == 0:
                primes.remove(j)
print(primes)
