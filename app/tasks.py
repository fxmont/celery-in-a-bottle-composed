
from itertools import combinations

import celery

app = celery.Celery(
    'dockerized-tasks',
    broker="amqp://admin:mypass@rabbit:5672",
    backend="redis://redis"
)


@app.task
def count_combinations(data, num):
    return sum(1 for _ in combinations(data, num))


@app.task
def divide(x, y):
    return x / y
