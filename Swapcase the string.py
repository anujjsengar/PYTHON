#Complete the swap_case function in the editor below.
#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
def swap_case(s):
    x=""
    for i in s:
        if i.isupper:
            x=x+i.lower()
        elif i.islower():
            x=x+i.upper()
        else:
            x=x+i
    return x
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
