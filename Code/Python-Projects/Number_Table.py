number = (int(input('Enter a number: ')))
for i in range(1, 13):
    if number in range(1, 13):
        print(number, 'x', i, ': ', number*i)  
else:   
    print('out of range')  


def main():
     
# end main