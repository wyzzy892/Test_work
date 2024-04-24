def computers(x:int):
    # Выводить слово взависимости от последней цифры
    word = None
    if x%10 == 1:
        word = "компьютер"
    elif x%10 >= 2 and x%10 <=4:
        word =  "компьютера"
    else:
        word =  "компьютеров"
    return f"{x} {word}"


if __name__=="__main__":
    try:
        x = int(input())
        print(computers(x))
    except ValueError:
        print("x must be an integer!")
