import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def add(a, b):
    logger.info(f"Сложение: {a} + {b}")
    return a + b

def divide(a, b):
    if b == 0:
        logger.error("Попытка деления на ноль!")
        raise ValueError("На ноль делить нельзя")
    return a / b


if __name__ == "__main__":
    print("Запуск программы...")

    res = add(10, 5)

    print(f"Результат в консоли: {res}")
