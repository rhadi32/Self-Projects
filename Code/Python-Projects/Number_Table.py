while True:
    number = (int(input('Enter a number: ')))
    for i in range(1, 13):
        if number not in range(1, 13):
            print('out of range')
        else:
            print(number, 'x', i, ': ', number*i)
