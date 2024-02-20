

print("Lolek polek molek")


my_list = [1,2,3,5]
print(len(my_list))

name = input("Jak sie nazywasz?: ")
print("Siemanko ", name)


for i in range(5):
    print(i)

numbers = [1,2,3,4,5,6,7]
total = sum(numbers)
print(total)


z = input("Podaj z :")
b = input("Podaj b :")

print("Z to : ",z,"a B to: ",b)

Cena_global = 10
def Test():
    Banan = 5
    global Cena_global
    Cena_global +=20
    print("Lokalny produkt: ", Banan)
    print("Globalna cena: ", Cena_global)

Test()

def przywitanie(a,b) :
    return a+b

def call_func(func, a,b):
    return func(a,b)

print(call_func(przywitanie, z,b))


