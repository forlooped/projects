print("This is the palindrome test using an if statement:")

j = "hoohooh"
print("The word is " + str(j))
if str(j) == str(j)[::-1]:
    print("Yes, " + j + " is a palindrome!")
else:
    print("No, " + j + " is not a palindrome :b")

print("\n")
print("This is the palindrome test using a class")

class checkit:
    def __init__(self, wordis):
        self.word=(wordis)
    def theCheck(self):
        if self.word == self.word[::-1]:
            print("Yay, " + self.word + " is a palindrome")
        else:
            print("Nope, " + self.word + " is not a palindrome :b")

hey = checkit("huha")
hey.theCheck()
