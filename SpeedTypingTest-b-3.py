import random
import time

# List of words for the typing test
word_list = ["python", "programming", "keyboard", "developer", "speed", "challenge", "practice", "coding", "algorithm", "challenge"]

# Function to display random word for typing test
def get_random_word():
    return random.choice(word_list)

# Function to run the typing test
def typing_test():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")
    word_to_type = get_random_word()
    print("Word to type: ", word_to_type)
    start_time = time.time()
    user_input = input("Type the word: ")
    end_time = time.time()
    typing_time = end_time - start_time

    if user_input.strip() == word_to_type:
        print(f"Congratulations! You typed the word correctly in {typing_time:.2f} seconds.")
    else:
        print("Oops! You made a mistake. Keep practicing!")

# Main function
def main():
    while True:
        typing_test()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thank you for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
