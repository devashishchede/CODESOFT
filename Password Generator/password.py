import random
import string

def generate_password(length=12, use_digits=True, use_specials=True):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters")
    
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_specials:
        chars += string.punctuation

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
    ]
    if use_digits:
        password.append(random.choice(string.digits))
    if use_specials:
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(chars)) 

    random.shuffle(password)
    return ''.join(password)