def process_string(s: str) -> tuple:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = {chr(c) for c in range(ord('a'), ord('z') + 1)} - vowels
    vowels_in_s = sorted({char for char in s if char in vowels})
    consonants_in_s = sorted({char for char in s if char in consonants})
    has_digits = any(char.isdigit() for char in s)
    return ("".join(vowels_in_s), has_digits, "".join(consonants_in_s))

input_str = input("Введіть рядок: ")
result = process_string(input_str)
print(result)
