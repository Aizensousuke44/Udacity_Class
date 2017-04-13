# Monty Hall Problem(Optional)
# One car in one of three doors
# Guess right probability

from random import randint

def simulate(N):
    K = 0
    for _ in range(N):
        truth = randint(1, 3)
        guess1 = randint(1, 3)

        if truth == guess1:
            monte = randint(1, 3)
            # if first guess is right, monte must unequal truth
            while monte == truth:
                monte = randint(1, 3)
        else:
            # if truth != guess1, just one choice for monte
            monte = 6 - truth - guess1
        # one chance to change
        guess2 = 6 - guess1 - monte

        if guess2 == truth:
            K += 1

    return K / N

if __name__ == '__main__':
    N = 1000
    print(simulate(N))
