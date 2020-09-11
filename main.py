import random
from datetime import datetime

from src import (
    LinkedList
)


if __name__ == '__main__':
    obj: LinkedList = LinkedList()
    random.seed(datetime.now())

    for _ in range(6):
        obj.insert(random.randint(0, 50))

    print(obj)

    obj.pop(0)
    print(obj)
    obj.pop(3)
    print(obj)