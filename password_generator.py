import random
import string

def generate_password():
    print("--- CodSoft Python Password Generator ---")
    
    try:
        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length of the password: "))
        if length < 4:
            print("Password length should be at least 4 characters for security.")
            return
    except ValueError:
        print("Please enter a valid numerical number for the length.")
        return

    # Character sets to use for generation (Letters, numbers, and symbols)
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters to specify the complexity
    all_characters = letters + digits + symbols

    # Use random choices to generate a password of the specified length
    password = "".join(random.choice(all_characters) for _ in range(length))

    # Display the generated password on the screen
    print(f"\nYour Generated Password: {password}")

if __name__ == "__main__":
    generate_password()