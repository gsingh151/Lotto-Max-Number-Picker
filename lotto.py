import random

def lotto():
    arr = random.sample(range(1, 50), 7)
    return arr


if __name__ == "__main__":
    numbers = lotto()
    print(numbers)