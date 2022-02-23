
secret_guess_number="2"
guess=""
guess_count=0
guess_limit=4
out_of_guess = False

while guess != secret_guess_number and not(out_of_guess):
        if guess_count < guess_limit:
            guess = input("enter guess:")
            guess_count += 1
        else:
            out_of_guess = True



if out_of_guess:
     print("you lose")
else:
     print("you win")
