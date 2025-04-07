import random

# words for game
word_list = ["python", "elephant", "guitar", "computer", "ocean", "mystery", "immaculate", "rainbow", "adventure", "tree", "unnecessary", "great", "sock", "shoe", "imaginary", "lightning", "blasphemy", "extraordinary"]

def scramble_word(word):
#gives scarmbled word
  word = list(word)
  random.shuffle(word)
  return ''.join(word)

def play_game():
#runs the game
  word = random.choice(word_list) #a random word
  scramble = scramble_word(word) #scramble word
  print("Welcome to the Word Unscramble Game!")
  print(f"Unscramble this word: {scramble}")

  while True:
    guess = input("Your guess: ").strip().lower()
    if guess == word:
      print("Correct! You guessed the word!")
      break
    elif guess == "quit":
      print(f"The correct word was '{word}'. Better luck next time!")
      break
    else: 
      print("Incorrect. Try again or type 'quit' to exit.")
  
if __name__ == "__main__":
  play_game()




