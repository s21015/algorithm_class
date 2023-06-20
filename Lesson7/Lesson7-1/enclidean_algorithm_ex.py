def enclid(a, b):
    if b == 0:
        return a
    else:
        return enclid(b, a%b)

print("a≧bとなる自然数を入力してください")
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
n = enclid(a, b)
print("それらの数の最大公約数は", enclid(n, c))