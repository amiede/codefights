VedicTwoDigitMultiplication

Vedic "mathematics" offers some shortcuts and tricks for certain arithmetic operations, mainly for performing mental calculations faster.

An interesting shortcut for multiplying two two-digit numbers is achieved by multiplying the digits vertically and diagonally, as given in the following example: `56 * 23 = 1288` 
`5 6`
`2 3`
`---`
`5*2 | 5*3  + 6*2 |  6*3` (vertical left | two diagonals | vertical right)
`10 | 27 | 18` (__chunks after first calculation__)
`10 | 28 | 8` (carrying over decimals from right to left)
`12 | 8 | 8` (carrying over decimals from right to lef and result: 1288)
  
"|" means here to concatenate the digit groups

For this challenge you need to return an array of integers with the Vedic shortcut chunks after the first calculation step. Lets look at two examples to make things clearer.

### Example

For `VedicTwoDigitMultiplication(56,23)` you need to return `[10, 27, 18]`.

For `VedicTwoDigitMultiplication(42,42)` you need to return `[16, 16, 4]`.

Kapish? (As Nassim Taleb would say ;-))



[execution time limit] 5 seconds (coffee)

[input] integer a
Two-digit integer to be multiplied

[input] integer b
Two-digit integer to be multiplied

[output] array.integer
Digit chunks after the first calculation step (before performing the carrying)


### Tests
Input:
a: 56
b: 23
Expected Output:
[10, 27, 18]

Input:
a: 42
b: 42
Expected Output:
[16, 16, 4]

Input:
a: 99
b: 99
Expected Output:
[81, 162, 81]