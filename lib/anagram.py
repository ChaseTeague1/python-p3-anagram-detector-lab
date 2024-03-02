# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = sorted([letter for letter in word])
    
    def match(self, anagrams):
        match_anagrams = []
        for word in anagrams:
            if sorted([letter for letter in word]) == self.word:
                match_anagrams.append(word)
        return match_anagrams
