def print_formatted(number):
    # your code goes here
    width = len(format(number, 'b'))
    for i in range(1,number+1):
        decimal = str(i).rjust(width)
        octal = format(i,'o').rjust(width)
        hexadecimal = format(i,'X').rjust(width)
        binary = format(i,'b').rjust(width)
        print(decimal, octal, hexadecimal, binary)
        
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)