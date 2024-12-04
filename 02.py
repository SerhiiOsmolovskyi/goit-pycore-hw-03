import random

def get_numbers_ticket(min: int, max: int, quanttity: int) -> list:
    if min < 1 or max > 1000 or min > max or quanttity < 1 or quanttity > (max - min + 1):
        return []
    random_numbers = random.sample(range(min, max + 1), quanttity)
    return sorted(random_numbers)

lottery_numbers = get_numbers_ticket(1, 36, 6)
print("Ваші лотерейні числа:", lottery_numbers)