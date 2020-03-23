def sum_of_digits(n):
    sum = 0
    if(n < 0):
        n = -n
    while (n > 0):
        sum = sum + (n % 10)
        n = n//10
    return sum

def swap(n):
    lenght=len(n)
    s = 0
    for i in range(lenght//2):
        s=n[i]
        n[i]=n[lenght-1-i]
        n[lenght-1-i] = s
    return s


def to_digits(n):
    x = []
    while (n > 0):
        x.append(n%10)
        n = n//10
    swap(x)
    return x

def digits_count(n):
    counter = 0
    while (n > 0):
        counter = counter + 1
        n = n//10
    return counter

def to_number(n):
    x = 0
    lenght = len(n)
    for i in range(lenght):
        if (n[i] > 9):
            count = digits_count(n[i])
            for j in range(count):
                x = x * 10
            x = x + n[i]
        else:
            x = x * 10
            x = x + n[i]
    return x

def factoriel(n):
    fac = 1
    if (n == 0):
        return fac
    else:
        for i in range(1,n+1):
            fac = fac * i
        return fac

def fact_digits(n):
    if n == 0:
        return 1
    sum_fact = 0
    arr = to_digits(n)
    lenght_arr = len(arr)
    for j in range(lenght_arr):
        if arr[j] == 0:
            sum_fact += 1
        else:
            sum_fact = sum_fact + factoriel(arr[j])
    return sum_fact

def palindrome(n):
    n = str(n)
    lenght = len(n)
    for i in range(lenght//2):
        if (n[i] != n[lenght - i -1]):
            return False
    return True

def count_vowels(str):
    s = {'a','e','i','o','u','y','A','E','I','O','U','Y'}
    lenght = len(str)
    count = 0
    for i in range(lenght):
        if(str[i] in s):
            count = count + 1
    return count

def count_consonants(str):
    s = {'b','B','c','C','d','D','f','F','g','G','h','H','j'\
    ,'J','k','K','l','L','m','M','n','N','p','P','q','Q','r',\
    'R','s','S','T','t','v','V','w','W','x','X','z','Z'}
    lenght = len(str)
    count = 0
    for i in range(lenght):
        if(str[i] in s):
            count = count + 1
    return count

def char_histogram(str):
    hist = {}
    lenght = len(str)
    for i in range(lenght):
        if (str[i] in hist):
            hist[str[i]] = hist[str[i]] + 1
        else:
            hist[str[i]] = 1
    return hist

def sum_matrix(m):
    lenght = len(m)
    sum1 = 0
    for i in range(lenght):
        sum1 = sum1 + sum(m[i])
    return sum1

def nan_expend(n):
    str = ""
    if n == 0:
        return str
    else:
        str = ("Not a " * n) + "NaN"
    return str

def prime_factorization(n):
    if n == 1:
        return [(1,1)]
    i = 1
    arr = factorizate(n)
    lst = []
    count = 0
    prime = 0
    for i in (arr):
        if (i == prime):
            count += 1
        else:
            if prime!= 0:
                lst.append((prime, count))
            prime = i
            count = 1
    lst.append((prime, count))

    return lst

def factorizate(x):
    factors = []
    i = 2
    while x > 1:
        if x % i == 0:
            x = x // i
            factors.append(i)
        else:
            i += 1
    return factors

def group(n):
    arr = []
    for i in range(len(n)):
        if i == 0:
            arr.append([n[i]])
        else:
            if n[i] == n[i-1]:
                arr[-1] += [n[i]]
            else:
                arr.append([n[i]])
    return arr

def max_consecutive(n):
    lenght = 0
    arr = group(n)
    for i in arr:
        if lenght < len(i):
            lenght = len(i)
    return lenght




