# https://codefights.com/arcade/intro/level-3/3o6QFqgYSontKsyk4
# Bought hint from grey_h :-\
def reverseParentheses(s):

    for i in range(len(s)):
        if s[i] == "(":
        # Find start of parentheses
            start = i
        if s[i] == ")":
        # Find end of parentheses
            end = i
            left = s[:start]
            middle = s[start+1:end] # Between () to be reversed
            print(middle)
            right = s[end+1:]
            # Recursive
            return reverseParentheses(left + middle[::-1] + right)
        
    return s