print('Hello from main!')
from dotenv import load_dotenv
import os

def print_author():
    # Загрузка переменных из .env файла
    load_dotenv()

    # Чтение переменной AUTHOR
    author = os.getenv('AUTHOR')

    # Печать имени автора
    print(f"Автор проекта: {author}")

# Вызов функции
print_author()
