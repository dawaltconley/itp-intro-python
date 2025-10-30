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
