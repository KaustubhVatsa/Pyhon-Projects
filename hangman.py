# a game of hangman where user gets 6 lives to guess a word.
import random
# global variables
wordList = {
    "easy": [
        "cat", "dog", "sun", "tree", "book",
        "ball", "fish", "moon", "star", "apple"
    ],

    "medium": [
        "planet", "python", "window", "guitar",
        "castle", "forest", "yellow", "bridge",
        "bottle", "silver"
    ],

    "hard": [
        "astronomy", "hangman", "difficult",
        "microscope", "philosophy",
        "architecture", "xylophone",
        "psychology", "cryptography"
    ]
}

# random word selection


def randomWord(difficulty):
    randomWordSelected = ""
    lives = 0
    match difficulty:
        case "easy":
            randomWordSelected = random.choice(wordList["easy"])
            lives = 6
        case "medium":
            randomWordSelected = random.choice(wordList["medium"])
            lives = 4
        case "hard":
            randomWordSelected = random.choice(wordList["hard"])
            lives = 2
    return randomWordSelected, lives

# select difficulty


def selectDifficulty():
    difficultyInput = input(
        "Please select your difficulty : choose from :  \neasy \nmedium \nhard \nPlease Input your choice : ").strip().lower()
    while (difficultyInput not in {"easy", "medium", "hard"}):
        difficultyInput = input(
            "Invalid choice : choose from :  \neasy \nmedium \nhard \nPlease Input your choice : ").strip().lower()
    return difficultyInput


# game logic
def game():
    difficulty = selectDifficulty()
    wordSelected, lives = randomWord(difficulty)
    gameOver = False
    display = ["_"] * len(wordSelected)
    allguessed = len(wordSelected)
    allChoices = set()
    while not gameOver and lives != 0:
        print("\nTotal Lives left : ", lives)
        print(" ".join(display))
        playerChoice = input("Please enter the character : ").lower().strip()
        validChoice = False
        if (playerChoice in allChoices):
            print("Already selected this character!! Please choose another one")
            continue
        for index, character in enumerate(wordSelected):
            if playerChoice == character:
                validChoice = True
                display[index] = character
                allguessed -= 1
                allChoices.add(playerChoice)

        if not validChoice:
            lives = lives-1
        if allguessed == 0:
            print("You Won !!")
            print(wordSelected)
            gameOver = True


game()
