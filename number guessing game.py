import random 
print("       
Welcome to the Mind Reader Game") 
name = input("Enter your name: ") 
print(f"\nHello {name}, choose your difficulty level:") 
print("1. Easy (1 - 50) | 10 lives") 
print("2. Medium (1 - 100) | 7 lives") 
print("3. Hard (1 - 200) | 5 lives") 
choice = int(input("Enter choice (1/2/3): ")) 
if choice == 1: 
max_range = 50 
lives = 10 
elif choice == 2: 
max_range = 100 
lives = 7 
elif choice == 3: 
max_range = 200 
lives = 5 
else: 
print("Invalid choice! Defaulting to Medium       
max_range = 100 
lives = 7 
secret_number = random.randint(1, max_range) 
score = 0 
") 
print(f"\nI have chosen a number between 1 and {max_range}. Can you guess it?") 
while lives > 0: 
    try: 
        guess = int(input(f"\nEnter your guess (Lives left: {lives}): ")) 
        if guess < 1 or guess > max_range: 
            print("   Stay inside the range!") 
            continue 
        if guess == secret_number: 
            score += lives * 10 
            print("              Boom! You got it!") 
            print(f"  Your score: {score}") 
            break 
        elif guess < secret_number: 
            print("    Too low!") 
        else: 
            print("    Too high!") 
        if random.choice([True, False]): 
            diff = abs(secret_number - guess) 
            if diff <= 5: 
                print("   You're VERY close!") 
            elif diff <= 15: 
                print("      Getting warmer...") 
            else: 
                print("           Way off!") 
        lives -= 1 
    except ValueError: 
        print("  Numbers only please!") 
if lives == 0: 
print("\n      
Game Over!") 
print(f"The number was: {secret_number}") 
print(f"Better luck next time, {name}         
")
