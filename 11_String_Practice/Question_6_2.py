text=input("Enter a word to check if it is a palindrome.\n")
text=text.lower()
a=text[::-1]
if (text==a):
    print("Yes, it is a palindrome.")
else:
    print("No, it's not a palindrome.")