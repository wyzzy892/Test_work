def common(arr):
    commons = []  # массив для общих делителей
    # начинаем с двойки до минимального значения в массиве
    for num in range(2, min(arr)+1):
        is_common_divisor = True
        for idx, value in enumerate(arr):
            # если число не делиться нацело можно не продолжать
            if value % num != 0:
                is_common_divisor = False  # отмечаем флаг, что общих делителей нет
                break
        # если общий делитель есть, то добавляем в массив
        if is_common_divisor:
            commons.append(num)

    return commons


if __name__=="__main__":
    try:
        arr = list(map(int, input().split()))
        print(common(arr))
    except ValueError:
        print("input must be an integer array!")