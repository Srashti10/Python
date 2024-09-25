def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome('radar'))
print(is_palindrome('hello'))
print(is_palindrome('Hello'))  # output will be false 
