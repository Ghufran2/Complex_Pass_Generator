import random
import string

def generate_complex_password(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    
    # Define character sets for the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Ensure the password has at least one character from each set
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special),
    ]
    
    # Fill the rest of the password length with random choices from all character sets
    password += random.choices(all_characters, k=length-4)
    
    # Shuffle the list to ensure the characters are in random order
    random.shuffle(password)
    
    # Convert the list to a string and return
    return ''.join(password)

# Example usage
password = generate_complex_password(12)
print(f"Generated Password: {password}")
