import textwrap

def wrap(string, max_width):
    #method1
    return textwrap.fill(string,max_width)
    
    #method2
    # result = ""
    # for i in range(0, len(string), max_width):
    #     result += string[i:i+max_width] + "\n"
    # return result.rstrip()  # remove the final extra newline

    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)