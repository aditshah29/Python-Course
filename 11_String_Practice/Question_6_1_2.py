sentence=input("Enter a sentence to count number of vowels in it:\n")
sum=0
vowels=['a', 'e', 'i', 'o', 'u']
for char in sentence.lower():
    if (char in vowels):
        sum+=1
print(f"There are {sum} number of vowels in the sentence.")