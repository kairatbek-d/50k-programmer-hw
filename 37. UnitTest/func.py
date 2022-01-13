def my_sum(a, b):
    try:
        return a+b
    except TypeError as e:
        raise TypeError(f'Error: {e}')

if __name__ == "__main__":
    print(my_sum(1, 2))