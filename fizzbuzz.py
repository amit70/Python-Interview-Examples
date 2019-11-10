#Write a program that outputs the string representation of numbers from 1 to n.

#But for multiples of three it should output “Fizz” instead of the number and for the
# multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

def fizzBuzz(A):
        output = []
        for number in range(1, A + 1):
            if number % 3 == 0 and number % 5 == 0:
                output.append('FizzBuzz')
            elif number % 3 == 0:
                output.append('Fizz')
            elif number % 5 == 0:
                output.append('Buzz')
            else:
                output.append(str(number))
        return output

print fizzBuzz(5)
