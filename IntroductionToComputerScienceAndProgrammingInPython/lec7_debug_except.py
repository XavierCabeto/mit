##def rev_list_buggy(L):
##    for i in range(len(L)):
##        j = len(L) - i
##        L[i] = temp
##        L[i] = L[j]
##        L[j] = L[i]

def rev_list(L):
    for i in range(len(L)//2):
        j = len(L) - i - 1
        temp = L[i]
        L[i] = L[j]
        L[j] = temp
        
L = [1,2,3,4]
rev_list(L)
print(L)

##def primes_list_buggy(n):
##    if i == 2:
##        primes.append(2)
##    for i in range(len(primes)):
##        for j in range(len(n)):
##            if i%j != 0:
##                primes.append(i)

def primes_list(n):
    primes = [2]
    for j in range(3,n+1):
        is_div = False
        for p in primes:
            if j%p == 0:
                is_div = True
        if not is_div:
            primes.append(j)
    return primes

print(primes_list(2) )               
print(primes_list(15)  )              

#a = int(input("Tell me one number: "))
#b = int(input("Tell me another number: "))
#print("a/b = ", a/b)
#print("a+b = ", a+b)

try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a/b)
except:
    print("Bug in user input.")

try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a/b)
    print("a+b = ", a+b)
except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Something went very wrong.")

def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i] """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number
        except:
            raise ValueError('get_ratios called with bad arg')
        else:
            print("success")
        finally:
            print("executed no matter what!")
    return ratios
    
print(get_ratios([1, 4], [2, 4]))

def get_stats(class_list):
	new_stats = []
	for person in class_list:
		new_stats.append([person[0], person[1], avg(person[1])])
	return new_stats 

#def avg(grades):
#    return (sum(grades))/len(grades)
    
def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('warning: no grades data')
        return 0.0

def avg(grades):
    assert len(grades) != 0, 'warning: no grades data'
    return sum(grades)/len(grades)
    
test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]], 
              [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
              [['captain', 'america'], [80.0, 70.0, 96.0]],
              [['deadpool'], []]]

print(get_stats(test_grades))
