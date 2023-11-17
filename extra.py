print('self_report as a game: ')
def my_grade():
    grade = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("This prints my expectation for my grade!")
    print("I'm thinking of a number between 1 and 10.")
    number = grade

    while True:
        guess = int(input("What's your guess? "))
        if guess == 7:
            print("You guessed it! The grade is 7.".format(number))
            break
        elif guess < 7:
            print("Too low! I deserve more than that")
        else:
            print("Too high! It is not that perfect!")
        continue
    question = input("Do you wanna know why? ")

    if question == "yes":
        print("Because although I know the codes are far from being perfect, but I tried my best. Therefore I hope at least the basics you wanted to test are more than 90% covered")
        print("That gives me a passing grade, a 6. However, I do feel like some stuffs you were asking in the question are more adventurous, so if I have answer that part of the questions right, I think there should be some extra points for that")
        print("and just to be honest and most importantly, I need more than 7 to pass the class. I do love python and I put a lot work into this semester for it so I don't want to do it again next year" )
        print("I have all the comments you wanna know in self-report written in the code script, because I found it much efficient and saving time from doing redundant actions ")

    else:
        print("Okay, farewell!")

if __name__ == "__main__":
    my_grade()
