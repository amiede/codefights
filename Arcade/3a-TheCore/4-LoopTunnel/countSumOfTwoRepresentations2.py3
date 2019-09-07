# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/hBw5BJiZ4LmXcy92u
def countSumOfTwoRepresentations2(n, l, r):
    return max(0, n//2 - max(l-1, n-r-1))

''' Comment by phil_p8
Given any number n there are only Math.floor(n/2) uniques integer sums that add to n. 
For n = 10 they would be as follows:
1-9
2-8
3-7
4-6
5-5
Now the second part of the equation is figuring out where you have lost more pairs. 
if L is 4 all of the following pairs:
1-9
2-8
3-7
Now what if r is 9? You only lose one pair:
1-9
From this you can see that it only matters what bound is removing the most possible pairs. The only thing that remains is what happens if there are no pairs. In test three you can see that an L > n/2 removes all possible pairs. In the equation these situations are negative and will then be converted into 0 via the max function.

'''