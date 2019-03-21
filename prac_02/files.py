"""
Asks user for name and stores it in a file
"""

name = str(input("What is your First name? : "))
OUTPUT_FILE = "name.txt"
output_file = open(OUTPUT_FILE, 'w')
print(name, file=output_file)
output_file.close()


""" 
Opens file and reads name and prints a sentence using the name
"""

your_name = open("name.txt", "r")
print("Your name is {}".format(your_name))
your_name.close()

"""
Creates a .txt file and and prints numbers to it 
"""

number_file = open("numbers.txt","w")
print("17\n42", file=number_file)
number_file.close()


"""
Opens .txt file and reads numbers and prints the summation 
"""

numbers = open("numbers.txt","r")
first_number = int(numbers.readline())
second_number = int(numbers.readline())
sum = first_number +second_number
numbers.close()
print("The total of the first 2 lines is: {}".format(sum))


"""
Opens .txt file and sums all numbers
"""

numbers = open("numbers.txt","r")
total = 0
for line in numbers:
    number = int(line)
    total += number
numbers.close()
print("The total of all integers on each line is: {}".format(total))