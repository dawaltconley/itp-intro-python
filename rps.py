# Goal: Make a rock-paper-scissors game using the `input` function

from random import randint

# Use a tuple to define the possible values
RPS = ('rock', 'paper', 'scissors')

# Use a dictionary to define what beats what
BEATS = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock',
}

# Generates a random rock/paper/scissors value
def get_random_rps():
    return RPS[randint(0, 2)]

# Compares two RPS values, returning the winner, or None if it's a tie
def get_winner(p1, p2):
    if BEATS[p1] == p2:
        return p1
    elif BEATS[p2] == p1:
        return p2
    elif p1 == p2:
        return None
    else:
        raise ValueError(f'Bad values compared: {p1} and {p2}')

# Converts a string to the nearest RPS value
def get_rps(string):
    if (string in RPS):
        return string
    for val in RPS:
        if val.startswith(string):
            return val
    return None

# Plays the game using user input
def play():
    user_score = 0
    comp_score = 0
    while True:
        user_input = input('Your move (r/p/s): ')
        user_play = get_rps(user_input)
        if user_play == None:
            print('Bad input, try again...')
            continue
        comp_play = get_random_rps()
        print('Computer:', comp_play)
        winner = get_winner(user_play, comp_play)
        if winner == user_play:
            print('You win!', ' ')
            user_score += 1
        elif winner == comp_play:
            print('You lose!', ' ')
            comp_score += 1
        else:
            print('Tie!', ' ')
        print(f'{user_score}:{comp_score}')

# Initiate the game
play()
