from functools import reduce

def is_even(a):
    return a%2==0


nums=[32,4,5,6,7,54,21,45]


nums1_to_100=[x for x in range(1,101)]
evens=list(filter(lambda a: a%2==0,nums1_to_100))

doubles=list(map(lambda a: a*a , nums1_to_100))

sum=reduce(lambda a,b : a+b , doubles)

print(sum)
print(doubles)
print(type(evens))
print(evens)

def square(num):
    return num*num

f= lambda a: a*a
print(square(10))


print(__name__)
