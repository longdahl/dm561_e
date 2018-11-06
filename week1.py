

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

def task5(*args):
    pass
def task6(*args):
    pass
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
    d = dict()
    for i in range(1,10):
        d[i] = [None]
    d[1] = [3] #values must be in lists so they are iterable
    d[2] = 1,2,3,4,5
    d[3] = ["1regninger regninger2"]

    for i in range(1,10):
        x = "task" + str(i)
        print("testing " + x +":")
        y = d.get(i)
        print("result is: " + str(globals()[x](*y)))
