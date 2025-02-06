def process_string(s: str) -> tuple:
    # Створюємо множини голосних і приголосних англійського алфавіту
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = {chr(c) for c in range(ord('a'), ord('z') + 1)} - vowels
    
    # Визначаємо голосні і приголосні літери у вхідному рядку
    vowels_in_s = sorted({char for char in s if char in vowels})
    consonants_in_s = sorted({char for char in s if char in consonants})
    
    # Перевіряємо, чи є цифри у вхідному рядку
    has_digits = any(char.isdigit() for char in s)
    
    # Формуємо вихідний кортеж
    return ("".join(vowels_in_s), has_digits, "".join(consonants_in_s))

# Отримання введення від користувача
input_str = input("Введіть рядок: ")
result = process_string(input_str)
print(result)