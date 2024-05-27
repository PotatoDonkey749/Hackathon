import re
with open("./input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        word = re.sub(r'[^a-zA-Z0-9]', '', line.strip().lower())
        reverse = word[::-1]
        is_palindrome = word == reverse
        unique = ''.join(set(word))
        print(f'{"YES" if is_palindrome else "NO"}, {"-1" if not is_palindrome else len(unique)}')
