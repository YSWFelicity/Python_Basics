'''
Sample Solution
CS 5001, Fall 2021 - HW4 problem 2
'''


def hide_answer(answer):
    '''
        Function -- hide_answer
            Helper function to create the hidden version of the word.
        Parameter:
            answer -- the word to hide
        Returns:
            The word with all characters replaced with "_"
    '''
    HIDE_CHAR = "_"
    return HIDE_CHAR * len(answer)


def is_letter_guess(guess):
    '''
        Function -- is_letter_guess
            Determines if the user's guess is a single character.
        Parameter:
            quess -- The user's guess
        Returns:
            True if the guess is a single charater, False otherwise.
    '''
    return len(guess) == 1


def process_word_guess(answer, current, guess):
    '''
        Function -- process_word_guess
            Checks to see if the user has guessed the correct word and updates
            the status of the secret word.
        Parameters:
            answer -- the secret word
            current -- the secret word with letters guessed so far revealed
            guess -- the user's guess
        Returns:
            The secret word after the user's guess has been processed. Letters
            that have already been guessed are visible. All other letters are
            replaced with an underscore.
    '''
    if is_correct(answer, guess):
        return answer
    return current


def process_letter_guess(answer, current, guess):
    '''
        Function -- process_letter_guess
            Checks to see if the user's guess is in the secret word and updates
            the status of the secret word.
        Parameters:
            answer -- the secret word
            current -- the secret word with letters guessed so far revealed
            guess -- the user's guess
        Returns:
            The secret word after the user's guess has been processed. Letters
            that have already been guessed are visible. All other letters are
            replaced with an underscore.
    '''
    i = 0
    while i < len(answer):
        if answer[i] == guess:
            current = current[:i] + guess + current[i+1:]
        i += 1
    return current


def already_guessed(guess, prev_guesses):
    '''
        Function -- already_guessed
            Determines if the user's guess is a letter they have already
            guessed.
        Parameters:
            guess -- the user's guess
            prev_guesses -- a string made up of the user's previous letter
            guesses.
        Returns:
            True if the user's guess has already been used, False otherwise.
    '''
    return guess in prev_guesses


def is_correct(answer, current):
    '''
        Function -- is_correct
            Checks if the secret word has been revealed.
        Parameters:
            answer -- the secret word
            current -- the word with guessed letters revealed.
        Returns:
            True if the user has guessed the word, False otherwise.
    '''
    return answer == current


def is_game_over(answer, current, guesses):
    '''
        Function -- is_game_over
            Checks if the round is over, either because the user has guessed
            the secret word or they have run out of guesses.
        Parameters:
            answer -- the secret word
            current -- the word with guessed letters revealed
            guesses -- the letters guessed so far
        Returns:
            True if the game is over, False otherwise.
    '''
    MAX_GUESSES = 6
    return is_correct(answer, current) or len(guesses) == MAX_GUESSES


def get_secret_word(game_round):
    '''
        Function -- get_secret_word
            Get's the secret word for the round.
        Parameters:
            game_round -- the current round, an integer between 1 and 3
            inclusive.
        Returns:
            The secred word for the round.
    '''
    if game_round == 1:
        return "APPLE"
    elif game_round == 2:
        return "OBVIOUS"
    else:
        return "XYLOPHONE"


def main():
    current_round = 1
    LAST_ROUND = 3
    player_wins = 0
    while current_round <= LAST_ROUND:
        word = get_secret_word(current_round)
        game_over = False
        letter_guesses = ""
        current = hide_answer(word)
        print(current)
        letter = input("Enter a letter or word: ").upper()
        while not game_over:
            if is_letter_guess(letter):
                if not already_guessed(letter, letter_guesses):
                    letter_guesses += letter
                    current = process_letter_guess(word, current, letter)
                else:
                    print("You've already guessed that letter!")
            else:
                current = process_word_guess(word, current, letter)
            game_over = is_game_over(word, current, letter_guesses)
            if not game_over:
                print(current)
                print("Your guesses so far:", letter_guesses)
                letter = input("Enter a letter or word: ").upper()
        if is_correct(word, current):
            print("You win!")
            player_wins += 1
        else:
            print("You lose! The word was", word)
        current_round += 1
    print("You won", player_wins, "out of", LAST_ROUND)


if __name__ == "__main__":
    main()
