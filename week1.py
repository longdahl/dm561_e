import math as m

def task1(r):
    return (4/3)*3.14159*r**3
def task2(a,b,c,d,e):
    print(a, b, str(c) + " " + str(d) + " " + str(e), sep='    ')

def task3(a):
    a = first_half(a)
    return backward(a)
def task4(*args):
    x = ["bear", "ant", "cat","dog"]
    x.append("eagle")
    x[2] = "fox"
    x.pop(1)
    x.sort(reverse=True)
    i = x.index("eagle")
    x[i] = "hawk"
    x[-1] += " hunter"
    return x

def task5(word):
    if type(word) != str or ' ' in word:
        raise TypeError("parameter must be word, ie. a string not containing spaces")
    vowel = "aeiouy"
    print(word)
    if vowel.__contains__(word[0]):
        return word + "hay"
    else:
        return word[1::] + word[0] + "ay"
def task6(*args):

    """

    #sort backwards from 999*999 in increments of 11.
    #see if palindrome then:
        - factorize
        - make 2, 3 digit numbers if possible
    """

    max = 998001# 999**2
    max -= max % 11 #even digit palindromes are divisible by 11
    for i in range(max,100000,-11):
        if str(i) == str(i)[::-1]:
            fact_list = factorize(i,[])
            a,b = make_3_digit(fact_list)
            if 1000 > a > 99 and 1000 > b > 99: # check probably not nececary
                break
    return a,b,a*b

def factorize(num,fact_list):
    i = 1 if num % 2 else 2
    for n in range(1+i,m.ceil(m.sqrt(num)),i):
        if num % n != 0:
            continue
        else:
            fact_list.append(n)
            return factorize(num/n,fact_list)
    fact_list.append(int(num))
    return fact_list
def make_3_digit(fact_list):
    a = fact_list[-1]
    b = 1
    for n in fact_list[0:-1]:
        if a*n < 1000:
            a *= n
        else:
            b *=n
    return a,b

def task7(*args):
    pass
def task8(*args):
    pass
def task9(*args):
    pass

def first_half(a):
    return a[0:len(a)// 2]

def backward(a):
    return a[::-1]

if __name__ == "__main__":

    #insert method parameters
    method_param = dict()
    for i in range(1,10):
        method_param[i] = [None]

    # insert test parameters below

    method_param[1] = [3] #values must be in lists so they are iterable
    method_param[2] = 1,2,3,4,5
    method_param[3] = ["1regninger regninger2"]
    method_param[5] = ["fish"]

    for i in range(1,10):
        x = "task" + str(i)
        print("testing " + x +":")
        y = method_param.get(i)
        print("result is: " + str(globals()[x](*y)))
