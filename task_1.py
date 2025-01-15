from pypred import Predicate
import re

# Регулярное выражение для поиска упоминаний "Черной пятницы"
black_friday_regex = re.compile(
    r'\b(?:'
    r'[чсмия4]?[еёэоаи]?рн[аоыяф]?[яе]?[йе]?'
    r'|'
    r'[чсмия4]?[оа]?рн[аоыяф]?[яе]?[йе]?'
    r')\s*'
    r'(?:'
    r'[пошщэ]?[яиыуоа]?[тгь]?[нм]?[иыуоа]?[цчс]?[аыуеё]?'
    r'|'
    r'[пошщэ]?[яиыуоа]?[тгь]?[нм]?[иыуоа]?[цчс]?[её]?'
    r')\b',
    re.IGNORECASE
)
# Правило для проверки наличия упоминания "Черной пятницы"
black_friday_rule = Predicate(
    """
    is_black_friday is True
    """
)


# Функция для проверки регулярного выражения
def check_black_friday(message):
    return bool(black_friday_regex.search(message))


# Примеры
messages = [
    "Добрый день! А до какого числа черная пятница будет действовать?",
    "Эта ваша чорная пятница мошейничество",
    "Где мой заказ?",
    "Черной пятнецы больше нет?"
]

# Проверка
for message in messages:
    is_black_friday = check_black_friday(message)

    # Контекст для правила
    context = {"is_black_friday": is_black_friday}

    # Проверка правила
    if black_friday_rule.evaluate(context):
        print(f"Сообщение: '{message}' - Упоминание Черной пятницы найдено.")
    else:
        print(f"Сообщение: '{message}' - Упоминание Черной пятницы не найдено.")
