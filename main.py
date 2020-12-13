def power(num, x=1):
    result = 1
    for i in range(x):
        result = result*num
    return result


if __name__ == '__main__':
    number = int(input('Please provide a number...'))
    indice = int(input('Please provide a power...'))
    print(power(number, indice))
2