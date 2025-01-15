import re

# Регулярное выражение для поиска упоминаний "Черной пятницы"
black_friday_regex = re.compile(
    r'\b(?:'
    r'[чс]?[еёэоаи]?рн[аоыяф]?[яе]?[йе]?'
    r'|'
    r'[чс]?[оа]?рн[аоыяф]?[яе]?[йе]?'
    r')\s*'
    r'(?:'
    r'[пошщэ]?[яиыуоа]?[тгь]?[нм]?[иыуоа]?[цчс]?[аыуеё]?'
    r'|'
    r'[пошщэ]?[яиыуоа]?[тгь]?[нм]?[иыуоа]?[цчс]?[её]?'
    r')\b',
    re.IGNORECASE
)

# Примеры сообщений
messages = [
    "Добрый день! А до какого числа черная пятница будет действовать?",
    "Эта ваша чорная пятница мошейничество",
    "Где мой заказ?",
    "Черной пятнецы больше нет?",
]

# Проверка
for message in messages:
    # Поиск совпадений с регулярным выражением
    if black_friday_regex.search(message):
        print(f"Сообщение: '{message}' - Упоминание Черной пятницы найдено.")
    else:
        print(f"Сообщение: '{message}' - Упоминание Черной пятницы не найдено.")