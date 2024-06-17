# Жадібний алгоритм


def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count

    return result


# Динамічне програмування


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    if dp[amount] == float("inf"):
        return {}

    result = {}
    current = amount
    while current > 0:
        coin = coin_used[current]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current -= coin

    return result


# Порівняння алгоритмів

import time

amount = 113344

start_time = time.time()
greedy_result = find_coins_greedy(amount)
greedy_time = time.time() - start_time

start_time = time.time()
dp_result = find_min_coins(amount)
dp_time = time.time() - start_time

print(
    f"Greedy algorithm result: {greedy_result}, time taken: {greedy_time:.10f} seconds"
)
print(f"Dynamic programming result: {dp_result}, time taken: {dp_time:.10f} seconds")
