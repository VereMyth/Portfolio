#Request the input words
first_name = input("type your name, and select enter:")
print("")
print("hello " + first_name + ". Let's play a game")
print("")
adjective1 = input("Tell me an adjective, and select enter.")
noun1 = input("Tell me a noun (plural), and select enter.")
noun2 = input("Tell me another noun (plural), and select enter.")
adjective2 = input("Tell me another adjective, and select enter.")
#part 2: Print the poem
print(first_name + "'s wacky Word Game")
print("")
print("Roses are " + adjective1)
print(noun1 + " are blue")
print(noun2 + " are " + adjective2)
print("And so are you!")

#Simple Calculator
num1=int(input("Enter a number:"))
num2=int(input("Enter another number:"))
choice = input ("Do you want to add, subtract, multiply, or divide>")
if chouce.upper() == "ADD":
    answer = num1 + num2
    print(num1, "+", num2, "=", answer)
if choice.upper() == "SUBTRACT":
        answer = num1 - num2
        print(num1, "-", num2, "=", answer)
if choice.upper() == "MULTIPLY":
        answer = num1 * num2
        print(num1, "*", num2, "=", answer)
if choice.upper() == "DIVIDE":
        answer = num1/num2
        print(num1, "/", num2, "=", answer)
else: print("invalid input, Sorry!")
               
            
