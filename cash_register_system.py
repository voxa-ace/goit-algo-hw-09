import timeit

def find_coins_greedy(amount, coins):
    """
    Function to find the number of coins needed for a given amount using a greedy algorithm.

    Parameters:
    amount (int): The total amount for which the change is required.
    coins (list): Sorted list of available coin denominations, in descending order.

    Returns:
    dict: A dictionary with keys as coin denominations and values as the number of coins of that denomination used.
    """
    result = {}
    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            result[coin] = num_coins
            amount -= num_coins * coin
    return result

def find_min_coins(amount, coins):
    """
    Function to find the minimum number of coins needed for a given amount using dynamic programming.

    Parameters:
    amount (int): The total amount for which the change is required.
    coins (list): List of available coin denominations.

    Returns:
    dict: A dictionary with keys as coin denominations and values as the number of coins of that denomination used.
    """
    min_coins = [0] + [float('inf')] * amount
    coins_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coins_used[i] = coin

    result = {}
    while amount > 0:
        coin = coins_used[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result

# Coin denominations
coins = [50, 25, 10, 5, 2, 1]

# Function to compare the execution time of both algorithms
def compare_execution_time(amount):
    """
    Compares the execution time of the greedy algorithm and dynamic programming algorithm.

    Parameters:
    amount (int): The total amount for which the change is required.

    Returns:
    tuple: A tuple containing execution times of greedy algorithm and dynamic programming algorithm.
    """
    greedy_time = timeit.timeit(lambda: find_coins_greedy(amount, coins), number=1000)
    dp_time = timeit.timeit(lambda: find_min_coins(amount, coins), number=1000)

    return greedy_time, dp_time

greedy_time, dp_time = compare_execution_time(1000)
print(f"Greedy Algorithm Time: {greedy_time:.5f} seconds")
print(f"Dynamic Programming Time: {dp_time:.5f} seconds")
