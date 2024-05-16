# Завдання 2

# Необхідно розробити функцію, яка приймає рядок як вхідний параметр, 
# додає всі його символи до двосторонньої черги (deque з модуля collections в Python), 
# а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. 
# Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, 
# а також бути нечутливою до регістру та пробілів.

from collections import deque
import re
s = input()

def is_palindrome(s):
    formatted_string = re.sub(r"\W+", "", s).lower()
    print(f"formatted: {formatted_string}")
    queue = deque(formatted_string)
    print(queue)

    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True

if is_palindrome(s) == True:
    print(f"Рядок '{s}' є паліндромом.")
else:
    print(f"Рядок '{s}' не є паліндромом.")

is_palindrome(s)
