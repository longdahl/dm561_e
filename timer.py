import timeit
import math as m
def reverse(str, aux=''):
    count = len(str)
    while count > 0:
        aux += str[count-1]
        count -= 1
    return aux

def palindrome(num):
    j = str(num)
    if j == reverse(j):
        return 1
    else:
        return 0
def benchmarkmethod():
    #downloaded from https://stackoverflow.com/questions/47999634/project-euler-largest-palindrome-product-of-two-3-digit-number
    i = 999
    max = 0
    while i > 99:
        j = 999
        while j > 99:
            num = i * j
            if palindrome(num):
                if num > max:
                    max = num
                    #print(max)
            j -= 1
        i -= 1


#another compare method

def c():
	max = maxI = maxJ = 0
	i = 999
	j = 990
	while (i > 100):
		j = 990
		while (j > 100):
			product = i * j
			if (product > max):
				productString = str(product)
				if (productString == productString[::-1]):
					max = product
					maxI = i
					maxJ = j
			j -= 11
		i -= 1
	return max, maxI, maxJ

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


def method_compare():
    print("result of my method")
    start = timeit.default_timer()
    task6()
    stop = timeit.default_timer()
    print('{:f}'.format(stop - start))
    print("result of compare method")
    start = timeit.default_timer()
    #benchmarkmethod()
    c()
    stop = timeit.default_timer()
    print(stop - start)
method_compare()
