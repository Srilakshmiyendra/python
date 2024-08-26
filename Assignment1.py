#1.Write a program which can filter even numbers in a list by using filter function. The list is: 
#[1,2,3,4,5,6,7,8,9,10].

n= [1,2,3,4,5,6,7,8,9,10]
def even_(x):
    return x%2==0
even_list = list(filter(even_,n))
print(even_list)
    
#2.Write a program which can map() to make a list whose elements are square of elements in 
#[1,2,3,4,5,6,7,8,9,10].
x = [1,2,3,4,5,6,7,8,9,10]
def sqr_(n):
    return n**2
sqr_list= map(sqr_,x)
print(list(sqr_list))

#3.Write a program which can map() and filter() to make a list whose elements are square of even 
#number in [1,2,3,4,5,6,7,8,9,10]
x = [1,2,3,4,5,6,7,8,9,10]
sqr= lambda n:n%2==0
sqr_=filter(sqr,x)
sqr_list = map(lambda n:n**2,sqr_)
print(list(sqr_list))

#4.Write a program which can filter() to make a list whose elements are even number between 1 and 
#20 (both included).

#x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def even_(n):
    return n%2==0
even= filter(even_,range(1,21))
print(list(even))

#5. Write a program which can map() to make a list whose elements are square of numbers between 
#1 and 20 (both included)
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sqr_ = lambda n: n**2
sqr_list= map(sqr_,x)
print(list(sqr_list))

#6.Define a class named American and its subclass NewYorker

class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican)
print(aNewYorker)

#7.Define a class named Rectangle which can be constructed by a length and width. The Rectangle 
#class has a method which can compute the area


class rectangle(object):
    def __init__(self, l, w):
        self.lenght = l
        self.width = w

    def area(self):
        return self.lenght*self.width

arectangle = rectangle(3,2)
print (arectangle.area())

#8.Write a function that returns the lesser of two given numbers if both numbers are even, but 
#returns the greater if one or both numbers are odd


def evenodd(n1,n2):
    if n1%2==0 and n2%2==0:
        if n1<n2:
            return n1
        else:
            return n2
    if n1%2==1 or n2%2==1:
        if n1>n2:
            return n1
        else:
            return n2
print(evenodd(2,9))  

#9.Write a function takes a two-word string and returns True if both words begin with same letter

def string(words):
    s1,s2=words.split()
    print(s1[0].upper()==s2[0].upper())
string("sri sri")    

#10.Write a function that capitalizes the first and fourth letters of a name

def word(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    #else:
       # return 'Name is too short'

result = word('abhiram')
print(result)