def is_palindrome(string):
    """Determine if "string" is a palindrome. Returns True if it is a palindrome, False if not."""

    # Base case: If the string is one character long or fewer, it's a palindrome.
    if len(string) <= 1:
        return True
    
    # Base case: If the first and last characters in the string don't match, it isn't a palindrome.
    if string[0] != string[-1]:
        return False
    
    # At this point, the first and last character in the string are identical.
    # Recursive case: Check if the string remaining after removing the first and last character
    # is a palindrome. If so, this string is a palindrome too.
    return is_palindrome(string[1:-1])

# Load the list of words
infile = open("words.txt")

# Iterate through all words
for line in infile:
    # If one of the words is a palindrome, print it out
    if is_palindrome(line.strip()):
        print(line.strip())