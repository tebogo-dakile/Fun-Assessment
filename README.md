
---

# Problem - Fun Technical Test

This task involves creating and modifying several Python functions to solve specific problems. You are required to implement the functions according to the provided descriptions and write unit tests to verify their correctness.

## Functions to Implement

1. **Dog Years**  
   Calculate a dog's age in dog years based on the following rules:
   - For the first two years, each dog year equals 10.5 human years.
   - For each additional year (up to 20 human years), each dog year equals 4 human years.

   **Expected Output:**
   ```
   Input a dog's age in human years: 15
   The dog's age in dog's years is 73
   ```

2. **FizzBuzz**  
   Return a string with numbers from 1 to `num`, but replace multiples of three with "Fizz", multiples of five with "Buzz", and multiples of both with "FizzBuzz".
   
   **Expected Output:**
   ```
   fizzbuzz(15) => "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
   ```

3. **Word Lengths**  
   Create a program that takes a sentence and returns a dictionary where the keys are unique words and the values are the lengths of those words.

   **Expected Output:**
   ```
   Input a sentence: "Aunty Yankho is amazing"
   Output: {'Aunty': 5, 'Yankho': 6, 'is': 2, 'amazing': 7}
   ```

4. **Cube Sum**  
   Calculate the sum of the cubes of the digits in a number.

   **Expected Output:**
   ```
   cube_sum(123) => 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
   ```

## To Test

- You must create a test file called `test_my_tests.py` in the root directory. In this file, write unit tests for the functions.
- You can test the technical correctness of your code by running the following command:
  
  ```bash
  python3 -m unittest test_my_tests.py
  ```

**Note**: These tests (*unedited*) must succeed before you may submit the solution.

For reference on how to implement Python functions and tests, please refer to the official Python documentation: [https://docs.python.org/3/](https://docs.python.org/3/).

