import datetime


# Функция для вычисления времени доставки в минутах
def minutes_to_deliver(order_date, delivery_date):
    return int((datetime.datetime.fromisoformat(delivery_date) - datetime.datetime.fromisoformat(
        order_date)).total_seconds() / 60)


# Пример
order_date = "2023-10-01T12:00:00"
delivery_date = "2023-10-01T13:30:00"

result = minutes_to_deliver(order_date, delivery_date)
print(result)
