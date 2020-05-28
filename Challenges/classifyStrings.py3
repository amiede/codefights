# https://app.codesignal.com/challenge/AiXeyeX6pB8AvE2p6
# https://regex101.com/ :-D
# https://regex101.com/r/0pMpIz/1
#def classifyStrings(s):
# 200 
s, = eval(dir()[0])
R = re.search
b = R("[^aeiou?]{5}|[aeiou]{3}", s) # plain bad
c = R("^(?=.{2}?)[aeiou?]{3}(?=[^aeiou]{3})", s) # bad edge cases: aa?bbbb + aa?bbb?a?bbb?aa --> damn hack! :-\
m = R("(?=.{0,4}?)[^aeiou]{5}|(?=.{0,2}?)[aeiou?]{3}", s) # mixed, but includes also bad edge cases :-\
return "bad" if b or c else "mixed" if m else "good"


# Solution by hivacruz
# 148
#r = re.search
#s, = eval(dir()[0])
#return 'bad' if r('[aeiou]{3}|[^aeiou?]{5}|[aeiou]{2}\?[^aeiou]{4}',s) else 'mixed' if r('[aeiou?]{3}|[^aeiou]{5}',s) else 'good'