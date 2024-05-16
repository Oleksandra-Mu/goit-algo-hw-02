# Завдання 1

# Потрібно розробити програму, яка імітує приймання й обробку заявок:
# програма має автоматично генерувати нові заявки
# (ідентифіковані унікальним номером або іншими даними),
# додавати їх до черги, а потім послідовно видаляти з черги для "обробки",
# імітуючи таким чином роботу сервісного центру.


# У цьому псевдокоді використовуються дві основні функції:
# generate_request(), яка генерує нові заявки та додає їх до черги,
# та process_request(), яка обробляє заявки, видаляючи їх із черги.
# Головний цикл програми виконує ці функції, імітуючи постійний потік нових заявок та їх обробку.

import queue

def generate_request(request_queue, request_id):
    """Створити нову заявку"""
    request = f"Нова заявка: {request_id}"
    """Додати заявку до черги"""
    request_queue.put(request)
    print(f"Заявку {request_id} додано до черги")

def process_request(request_queue):
    if not request_queue.empty():
        """Видалити заявку з черги"""
        request = request_queue.get()
        """Обробити заявку"""
        print(f"Заявка {request} в обробці")

    else:
        print("Черга пуста")

def main():
    """Створюємо чергу заявок"""
    request_queue = queue.Queue()
    request_id = 0

    while True:
        generate_request(request_queue, request_id)
        process_request(request_queue)
