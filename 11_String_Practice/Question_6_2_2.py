string=input("Enter a word to check if it is a plaindrome.\n")
if (string==string[::-1]):
    print("It is a plaindrome.")
else:
    print("It is not a palindrome.")