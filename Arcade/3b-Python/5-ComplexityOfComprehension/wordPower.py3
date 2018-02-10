# https://codefights.com/arcade/python-arcade/complexity-of-comprehension/5rZN7nJ7Tkd9S4TLC
def wordPower(word):
    num = {power: string.ascii_lowercase.find(power)+1 for power in word}
    # num = {power: ord(power)-96 for power in string.ascii_lowercase}
	return sum([num[ch] for ch in word])
