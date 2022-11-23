"""Игра угадай число
Компьютер сам загадывает и сам угадывает число меньше чем за 20 попыток
"""

import numpy as np
def random_predict(number: int = 1) -> int:
    count = 0
    min_num = 1
    max_num = 100
    while count<10:
        count += 1
        avg=(min_num + max_num)//2
        if number == avg:
            break
        elif number>avg:
            min_num = avg + 1
        else:
            max_num = avg - 1
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
