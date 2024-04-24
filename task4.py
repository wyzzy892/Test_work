def table(x:int):
    # построчно выводим произведения чисел
    for i in range(0, x+1):
        if i == 0:
            for j in range(0, x+1):
                if j==0:
                    print(" \t", end=" ")
                else:
                    print(f"{j}\t", end=" ")
            print()
        else:
            for j in range(0, x+1):
                if j==0:
                    print(f"{i}\t", end=" ")
                else:
                    print(f"{j*i}\t", end=" ")
            print()


if __name__=="__main__":
    try:
        x = int(input())
        table(x)
    except ValueError:
        print("x must be an integer!")