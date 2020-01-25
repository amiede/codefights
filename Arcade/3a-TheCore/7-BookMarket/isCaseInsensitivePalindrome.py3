# https://app.codesignal.com/arcade/code-arcade/book-market/G9wj2j6zaWwFWsise
#def isCaseInsensitivePalindrome(inputString):
isCaseInsensitivePalindrome = lambda s: s.casefold() == s[::-1].casefold()