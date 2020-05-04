# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number and
# for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.

class whoa:
    def checking(self):
        three = range(0, 100, 3)
        five = range(0, 100, 5)

        for i in range(1, 100):
            if i in three:
                print("fizz")
            else:
                if i in five:
                    print("buzz")
                else:
                    print(i)
final = whoa()
final.checking()
