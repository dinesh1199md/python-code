def remove_adjacent_duplicates(s):
    while True:
        new_s = ""
        i = 0
        while i < len(s):
            # If adjacent characters are the same, skip them
            if i < len(s) - 1 and s[i] == s[i + 1]:
                while i < len(s) - 1 and s[i] == s[i + 1]:
                    i += 1
            else:
                new_s += s[i]
            i += 1
        if new_s == s:  # No more changes
            break
        s = new_s
    return s

# Test the function
input_str = "abccba"
output = remove_adjacent_duplicates(input_str)
print("Output:", output)
