def check_password_strength(password):
    special_chars = ['!','@','#','$','%','^','&','*','(',')','-','_']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    
    has_special = any(char in password for char in special_chars)
    has_number = any(char in password for char in numbers)
    is_long_enough = len(password) > 8
    
    if is_long_enough and has_special and has_number:
        return "Password is strongest"
    elif is_long_enough and has_special or is_long_enough and has_number:
        return "Password is stronger"
    elif has_special or has_number:
        return "Password is strong"
    else:
        return "Password is weak"

# Test the password
password = input("Enter a password: ")
result = check_password_strength(password)
print(result)