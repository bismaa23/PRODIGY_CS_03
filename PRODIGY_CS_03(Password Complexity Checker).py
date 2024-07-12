# Function to check if password meets minimum length requirement
def check_length(password):
    min_length = 8
    if len(password) >= min_length:
        return True  
    else:
        return False  

# Function to check if password has at least one uppercase letter
def has_uppercase(password):
    for char in password:
        if char.isupper():
            return True  
    return False  

# Function to check if password has at least one lowercase letter
def has_lowercase(password):
    for char in password:
        if char.islower():
            return True 
    return False  

# Function to check if password has at least one digit
def has_digit(password):
    for char in password:
        if char.isdigit():
            return True  
    return False  

# Function to check if password has at least one special character
def has_special_char(password):
    special_chars = "!@#$%^&*()_-+=<>?./"
    for char in password:
        if char in special_chars:
            return True 
    return False  

# Function to check password strength based on various criteria
def check_password_strength(password):
    length_check = check_length(password)
    uppercase_check = has_uppercase(password)
    lowercase_check = has_lowercase(password)
    digit_check = has_digit(password)
    special_char_check = has_special_char(password)

    # Evaluate password strength based on all criteria checks
    if length_check and uppercase_check and lowercase_check and digit_check and special_char_check:
        print("Password is strong!")  
    else:
        print("Password is weak. Please ensure it meets all criteria.") 

# Main function
def main():
    password = input("Enter your password: ")  
    check_password_strength(password)  

main()
