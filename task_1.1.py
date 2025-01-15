from pypred import Predicate

# Правило для проверки наличия упоминания "Черной пятницы"
black_friday_rule = Predicate(
    """
    message contains "черная пятница" or
    message contains "чёрная пятница" or
    message contains "черной пятницы" or
    message contains "чёрной пятницы" or
    message contains "черную пятницу" or
    message contains "чёрную пятницу" or
    message contains "чорная пятница" or 
    message contains "черной пятнецы" 
    """
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
    lower_message = message.lower()

    # Контекст для правила
    context = {"message": lower_message}

    # Проверка правила
    if black_friday_rule.evaluate(context):
        print(f"Сообщение: '{message}' - Упоминание Черной пятницы найдено.")
    else:
        print(f"Сообщение: '{message}' - Упоминание Черной пятницы не найдено.")