def search(string, substring):
    """Returns True if "substring" is contained within "string", and False otherwise"""

    # Outer loop: Iterate through every index in "string"
    for i in range(len(string)):

        # Inner loop: Iterate through every index in "substr"
        for j in range(len(substring)):

            # Are we trying to read past the end of "string"? If so, we definitely didn't
            # find the substring, and we can return False (we did not find the substring)
            if i + j >= len(string):
                return False

            # Otherwise, we aren't trying to read past the end of "string". We can compare
            # individual letters in the substring to individual letters in the string.

            # Is the current substring character (j) not equal to the equivalent string 
            # character (i+j)? If so, give up and try the next string character.
            if substring[j] != string[i+j]:
                break

            # If we have:
            #   1. Reached the end of the substring
            #   2. The current substring character and equivalent string character are identical
            # Then we found that the substring is contained within the string. Return True.
            if substring[j] == string[i+j] and j + 1 == len(substring):
                return True
    
    # If we reach this point, there was no match. Return False. This should be taken care of at
    # line 10, but nice to have just in case (
    return False

print(search("mango", "go"))