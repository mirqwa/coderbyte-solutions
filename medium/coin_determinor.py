# Have the function coin_determiner(num) take the input, which will be an integer ranging
# from 1 to 250, and return an integer output that will specify the least number of coins, that when added,
# equal the input integer. Coins are based on a system as follows: there are coins representing the integers
# 1, 5, 7, 9, and 11. So for example: if num is 16, then the output should be 2 because you can achieve the
# number 16 with the coins 9 and 7. If num is 25, then the output should be 3 because you can achieve 25 with
# either 11, 9, and 5 coins or with 9, 9, and 7 coins.


import sys


coins = [1, 5, 7, 9, 11]


def get_coin_count(num, max_index, start_index):
    count = 0
    if num > coins[max_index]:
        num -= coins[max_index]
        count += 1
    
    for i in range(start_index, -1, -1):
        while num >= coins[i]:
            num -= coins[i]
            count += 1
    
    return count


def coin_determiner(num):
    coins_count = sys.maxsize
    for i in range(len(coins) - 1, -1, -1):
        for j in range(i, -1, -1):
            count = get_coin_count(num, i, j)
            if count < coins_count:
                coins_count = count
    return coins_count


if __name__ == "__main__":
    print(coin_determiner(16))
    print(coin_determiner(25))
