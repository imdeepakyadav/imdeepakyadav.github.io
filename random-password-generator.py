import random
import string

# Function to generate a password of a given length
def generate_password(length: int) -> str:
    # Use the string module to get a list of valid characters
    valid_chars = string.ascii_letters + string.digits + string.punctuation

    # Use the random module to generate a random password
    password = ''.join(random.choice(valid_chars) for i in range(length))

    return password

# Example usage
password = generate_password(10)
print(password)
