import secrets
import string

def generate_password():
    ''' generates password according to a specified strength'''
    print("How strong do you ant your password to be?")
    strength = input("(Enter 'weak', 'strong', or 'very strong'): ").lower()
    if strength == 'weak':
        length = 5
    elif strength == 'strong': 
        length = 8
    elif strength == 'very strong':
        length = 12
    else:
        print("Invalid input. Please enter 'weak', 'strong', or 'very strong'")
        return
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    print(f"Your {strength} password is {password}")

generate_password()

    


    



