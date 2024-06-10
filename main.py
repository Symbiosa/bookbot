from collections import Counter
import pprint as pp
#Opens the book and stores the string inside variable
def main(): 
    with open("book/frankenstein.txt") as f: 
        fileContents = f.read()
        return fileContents
#New function to split book and return word count
def count():
    words = main().split()
    print(len(words))
#function to count each character
def chars():
    c = Counter(c for c in main().lower() if c.isalpha())
    for key, value in dict(c.most_common()).items():
        print(f"{key} decided to show up {value} times, yikes")
    
chars()
    