print("Count number of words in a line:")

print(len(input("What would you like to say: ").split(',')))

def count_vowel(str):
    count = 0
    vowel = set("aeiouAEIOU")
    
    for alphabet in str:
        if alphabet in vowel:
            count = count + 1
    
    print("Number of vowels: ", count)

str = input("What would you like to say: ")

count_vowel(str)
