import random

def lotto():
    arr = random.sample(range(1, 50), 7)
    print(arr)


if __name__ == "__main__":
    lotto()