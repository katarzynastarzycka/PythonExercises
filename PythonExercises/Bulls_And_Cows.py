

# Exercise 18: Cows and Bulls


# generate a 4-digit number
# ask the user to start guessing
# count guesses
# check how many digits are guessed correctly and how many should be in different place
#   and show the message to the user
# stop when the user guessed correctly
# show number of guesses


def convert_to_list(number):
    a = []
    for i in range(4):
        a.append(number % 10)
        number = number // 10
    a.reverse()
    return a


class UserActivity():
    def __init__(self):
        self.count_guesses = 1

    def number_to_guess(self):
        import random
        number = random.randint(1, 9999)
        return convert_to_list(number)


    def user_input(self):
        self.count_guesses += 1
        return int(input("Take a guess: \n"))


    def user_output(self, cows, bulls):
        if cows < 4:
            print("The result is {} cow(s) and {} bull(s).".format(cows, bulls))
        elif cows == 4:
            print("You have guessed the number! Congrats!")
            print("You needed {} guesses.".format(self.count_guesses))


class TestActivity():

    def __init__(self, test_number, test_input):
        self.test_number = test_number
        self.test_input = test_input
        self.i = 0
        self.actual_output = []

    def number_to_guess(self):
        return convert_to_list(self.test_number)


    def user_input(self):
        self.i += 1
        if self.i > len(self.test_input):
            raise AssertionError("Unexpected input")
        return self.test_input[self.i - 1]


    def user_output(self, cows, bulls):
        self.actual_output.append((cows, bulls))



def Cows_And_Bulls(activity):

    to_guess = activity.number_to_guess()

    print('The number between 1 and 9999 has been chosen. \n')   # jak to zmienić?

    not_guessed = True

    while not_guessed:
        cows = 0  # correct places
        bulls = 0  # remaining correct digits

        user_try = activity.user_input()
        guess = convert_to_list(user_try)

        index_list = [0, 1, 2, 3]

        for i in reversed(range(4)):
            if to_guess[i] == guess[i]:
                cows += 1
                del index_list[i] # remove that index from the list
        to_guess_limited = [to_guess[i] for i in index_list]
        guess_limited = [guess[i] for i in index_list]

        for i in range(len(index_list)):
            if guess_limited[i] in to_guess_limited:
                bulls += 1
                to_guess_limited.remove(guess_limited[i])

        if cows == 4:
            not_guessed = False

        activity.user_output(cows, bulls)


import unittest

class Test_Cows_And_Bulls(unittest.TestCase):

    def test_basic(self):
        activity = TestActivity(6789,[6789])
        Cows_And_Bulls(activity)
        self.assertEqual(activity.actual_output, [(4,0)])

    def test_basic2(self):
        activity = TestActivity(6789,[6780, 6798, 6789])
        Cows_And_Bulls(activity)
        self.assertEqual(activity.actual_output, [(3,0), (2,2), (4,0)])



if __name__ == '__main__':
    unittest.main()

