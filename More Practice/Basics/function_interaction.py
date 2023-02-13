def player_guess():

    guess=''

    while guess in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, or 2")

    return int(guess)



print(player_guess())