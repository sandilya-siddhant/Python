# Function to check if a number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Loop through numbers from 1 to 1000 and print prime numbers
for num in range(1, 1001):
    if is_prime(num):
        print(num)
