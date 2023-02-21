#CONVERSION TO ROMAN NUMBER
def r(n):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    a= 12
      
    while n:
        x = n// num[a]
        n%= num[a]
  
        while x:
            print(sym[a], end = "")
            x-= 1
        a-= 1
q=int(input())
r(q)
