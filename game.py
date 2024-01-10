import random
import time

def select_number(number_pool):
    """ Selects a random number from the pool and removes it. """
    number = random.choice(number_pool)
    number_pool.remove(number)
    return number

def main():
    number_pool = list(range(1, 70))  # Pool of numbers from 1 to 69
    selected_numbers = []

    print("Starting the lottery draw...")

    while len(selected_numbers) < 6:
        time.sleep(random.randint(3, 6))  # Random interval between 3 and 6 seconds
        number = select_number(number_pool)
        selected_numbers.append(number)
        print(f"Number drawn: {number}")

    print("\nLottery numbers:", selected_numbers)

if __name__ == "__main__":
    main()
