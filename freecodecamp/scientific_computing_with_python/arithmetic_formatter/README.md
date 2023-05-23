# Arithmetic Arranger

This module contains a function called `arithmetic_arranger` that takes a list of arithmetic problems and arranges them vertically and side-by-side.

```python
def arithmetic_arranger(problems, display_results=False, space_between_problems=4, minimal_distance=2, digit_limit=4):
```

## Parameters

- `problems`: A list of strings representing arithmetic problems. Each problem should contain two numbers and an operator (`+` or `-`) separated by spaces. For example: `"32 + 698"`.
- `display_results` (optional): A boolean value indicating whether or not to display the results of the arithmetic problems. Defaults to `False`.
- `space_between_problems` (optional): An integer value representing the number of spaces to insert between each problem. Defaults to `4`.
- `minimal_distance` (optional): An integer value representing the minimal distance between the operator symbol and the longest number length for each problem. Defaults to `2`.
- `digit_limit` (optional): An integer value representing the maximum number of digits allowed for each number in the problems. Defaults to `4`.

## Returns

The function returns a string containing the arranged problems. If any errors are encountered (e.g., too many problems, invalid operator, non-digit characters), an error message is returned.

## Example Usage

```python
problems = ["12 + 345", "-6789 - 123", "-456 + 789", "987 - 655", "-3210 + 4321"]
```

### Arithmetic output hidden
```python
print(arithmetic_arranger(problems))
```

Output:

```python
   12    -6789     -456      987     -3210
+ 345    - 123    + 789    - 655    + 4321
-----    -----    -----    -----    ------
```

### Arithmetic output displayed
```python
print(arithmetic_arranger(problems, display_results=True))
```
Output:

```python
   12    -6789     -456      987     -3210
+ 345    - 123    + 789    - 655    + 4321
-----    -----    -----    -----    ------
  357    -6912      333      332      1111
  ```
  
 ### How is the output generated?:
 
1. The function starts by checking if the number of problems is within the allowed range (between 1 and 5). If not, it returns an error message.
2. The problems are then split into three lists: `addends_1`, `operators`, and `addends_2`.
3. The function checks if the operators are supported (`+` or `-`). If not, it returns an error message.
4. The function then converts the addends to integers and checks if they contain only digits. If not, it returns an error message.
5. The results of the arithmetic operations are calculated and stored in a list called `results`.
6. The maximum length of each problem is calculated by finding the length of the longest addend and adding a minimal distance to account for the operator symbol and a single white space.
7. The function checks if any of the addends exceed the digit limit (4). If so, it returns an error message.
8. The addends and results are then padded with spaces to align them vertically.
9. The lines are constructed with fixed spacing between the problems.
10. Finally, the lines are joined together with newline characters to form the final output string.


## test_pytest.py
Custom pytest file to test the code.

# Credits
test_module.py was provided with the project
