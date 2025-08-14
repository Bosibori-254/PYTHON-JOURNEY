import random
import string


def generate_password(length=10, use_special_chars=True):
    letters = string.ascii_letters + string.digits
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ''
    all_chars = letters + digits + special_chars
    if numbers:
        characters = + digits
    if use_special_chars:
        all_chars += special_chars

        password = ''.join(random.choice(all_chars) for _ in range(length))
        meets_criteria = False
        has_numbers = False
         has_special_chars = False

          while not meets_criteria:
               password = ''.join(random.choice(all_chars)
                                   for _ in range(length))
                has_numbers = any(char.isdigit() for char in password)
                 has_special_chars = any(
                      char in special_chars for char in password)
                  meets_criteria = has_numbers and has_special_chars

                   if new_char in digits:
                        has_numbers = True
                    elif new_char in special_chars:
                        has_special_chars = True

                        meets_criteria = True
                        numbers:
                        meets_criteria = has_numbers and has_special_chars

                        if special_chars:
                            meets_criteria = has_numbers and has_special_chars

                            return password

                        min_length = int(
                            input("Enter minimum password length: "))
                        has_numbers = int(
                            input("Require numbers? (1 for Yes, 0 for No): "))
                        has_special_chars = int(
                            input("Require special characters? (1 for Yes, 0 for No): "))

                        password = generate_password(
                            min_length, has_numbers, has_special_chars)
                        print(f"Generated password: {password}")

    
