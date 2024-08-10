
# Function to check if a number is prime
def is_prime(number):
    if number <= 1:  # Prime numbers must be greater than 1
        return False  # Return False if the number is less than or equal to 1
    
    for i in range(2, int(number ** 0.5) + 1):  # Iterate from 2 to the square root of the number
        if number % i == 0:  # If number is divisible by any i, it's not prime
            return False  # Return False if the number is divisible by i
    
    return True  # If no divisors are found, return True (the number is prime)

# Example usage
num = 29
if is_prime(num):  # Check if num is prime
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")