words = ["hello", "world", "madam", "level"]

for word in words:
    if word == word[::-1]:
        print("First palindrome:", word)
        break
else:
    print("No palindrome found")
