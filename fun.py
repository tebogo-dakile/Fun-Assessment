def dog_years():
    
    """
    Create a program that counts a dog's age in dog's years. The program should only calculate dog years until 20 human years.
    Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

    Expected Output:
    ```
    Input a dog's age in human years: 15
    The dog's age in dog's years is 73
    ```
    """
def dog_years():
    human_age = int(input("Input a dog's age in human years: "))
    if human_age < 1 or human_age > 20:
        print("Age from 1 - 20")
    if human_age >= 1 <= 20:
        i = human_age - 2
        j = int(i * 4)
        dog_age = int((2 * 10.5) + j)
    print(f"Dog age is: {dog_age}")

dog_years()

def fizzbuzz(num):
    """
    Create a program that returns the numbers as a string from 1 to num. 
    But for multiples of three print “Fizz” instead of the number, 
    and for multiples of five print “Buzz”. For numbers which are 
    multiples of both three and five, print “FizzBuzz”.

    Expected Output:
    fizzbuzz(15) => "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
    """

  
def fizzbuzz(num):
    fizzbuzz =[]
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz.append("FizzBuzz")
        elif i% 3 == 0:
            fizzbuzz.append("Fizz")
        elif i % 5 == 0:
            fizzbuzz.append("Buzz")
        else:
            fizzbuzz.append(str(i))
    print(' '.join(fizzbuzz))
fizzbuzz(15)

    

def word_lengths(sentence):
    """
    Create a program that takes a sentence and returns a dictionary with each unique word
    as the key and the length of the word as the value.

    Expected Output:
    ```
    Input a sentence: "Aunty Yankho is amazing"
    Output: {'Aunty': 5, 'Yankho': 6, 'is': 2, 'amazing': 7}
    ```
    """
    
    #enter your code here

def cube_sum(number):
    """
    Create a program that calculates the sum of the cubes of each digit in a number.
    
    Expected Output:
    ```
    cube_sum(123) => 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
    ```
    """
    
    #enter your code here