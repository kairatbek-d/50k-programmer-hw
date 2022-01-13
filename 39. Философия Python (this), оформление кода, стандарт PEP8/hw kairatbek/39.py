def main ()   :
        a = int ( input())
        b = int(input( ) )
        c=a + b
        print(a +b)
        return a+ b

# main()

def myMain():
    try:
        first_number = int(input("Введите число:\n"))
        second_number = int(input("Ещё введите число:\n"))
        sum = first_number + second_number
        print(f"Сумма: {sum}")
    except ValueError:
        print("Пожалуйста, введите только числа")
    except KeyboardInterrupt:
        print("Введите число. Не покиньте терминал! Вернитесь!")

myMain()
