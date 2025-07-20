secret_password = "open123"
max_attempts = 3
attempts = 0

print("=== Password Guessing Game ===")
hint = "The password has 7 Characters and starts with 'o' ."
print(hint)

while attempts < max_attempts:
    guess = input("Enter Password: ")
    attempts += 1
    
    if guess == secret_password:
        print("Congratulations! You Guess The password correct.")
        break
    else:
        print("Password is incorrect.")
        
        if attempts < max_attempts:
                print(f"You have left attempt: {max_attempts - attempts}")
        else:
            print("Too many Incorrect.")    
print("Game Over!") 





   