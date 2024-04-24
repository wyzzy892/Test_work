def primes(a:int, b:int):
    # функция реализует алгоритм "Решето Эратосфена"
    # заводим массив с числами от 0 до b включительно
    nums = [i for i in range(0, b+1)]
    nums[1] = 0 # число 1 не считается простым => помечаем его нулем

    for idx in range(2, b+1):
        if nums[idx]!=0:  # если число не ноль, оно простое 
            k = 2*idx  # но число которое равно текущему * 2 - составное
            # индексы и числа совпадают, т.к. ряд чисел начинается с 0
            while k <= b: # все составные числа зануляем
                nums[k] = 0
                k += idx

    # отфильтровываем 0 и все числа меньше правой границы
    primes = list(filter(lambda x: x >= a, nums))
    return list(filter(lambda x: x!=0, primes))


if __name__=="__main__":
    try:
        a, b = list(map(int, input().split()))
        print(primes(a, b))
    except ValueError:
        print("a nad b must be an integer numbers!")