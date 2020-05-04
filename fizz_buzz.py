# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number and
# for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.

class whoa:
    def checking(self):
        three = range(0, 101, 3)
        five = range(0, 101, 5)

        for i in range(1, 101):
            if i in three and i in five:
                print("FizzBuzz")
            else:
                if i in three:
                    print("Fizz")
                else:
                    if i in five:
                        print("Buzz")
                    else:
                        print(i)
final = whoa()
final.checking()

