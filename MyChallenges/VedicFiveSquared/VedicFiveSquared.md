VedicFiveSquared

Vedic "mathematics" offers some shortcuts and tricks for certain arithmetic operations, mainly for performing mental calculations faster.

An interesting shortcut for squaring any number ending with a "5" is given by the following two examples:
  `125² = 12 * 13 | 5² = 156 | 25 = 15625` 
  
  `75² = 7 * 8 | 5² = 56 | 25 = 5625`
"|" means here to concatenate the digit groups

For this challenge you need to return an array of integers with the Vedic shortcut chunks of the first step. Lets look at two examples to make things clearer.

### Example

For `VedicFiveSquared(125)` you need to return `[12, 13, 25]`.

For `VedicFiveSquared(75)` you need to return `[7, 8, 25]`.

Kapish? (As Nassim Taleb would say ;-))

[execution time limit] 4 seconds (py3)

[input] integer number
Number to be squared, guaranteed to be ending with "5"

[output] array.integer
Digit chunks after the first calculation step (before assembling the final result)

### Tests
Input:
number: 125
Expected Output:
[12, 13, 25]

Input:
number: 75
Expected Output:
[7, 8, 25]

Input:
number: 25
Expected Output:
[2, 3, 25]

Input:
number: 255
Expected Output:
[25, 26, 25]

Input:
number: 5005
Expected Output:
[500, 501, 25]