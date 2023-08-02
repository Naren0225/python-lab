#divisible by 3 or not
my_cars1 = [9, 15, 10, 20, 27, 24, 66, 70] 
print("Numbers divisible by 3: ")
for i in my_cars1:
    if i%3==0:
        print(i)

#square the even numbers
my_cars1 = [9, 15, 10, 20, 27, 24, 66, 70]
print("square of even numbers: ")
for i in my_cars1:
    if i%2==0:
        print(i**2)
    
#sum of digits of all even numbers
my_cars1 = [9, 15, 10, 20, 27, 24, 66, 70]
print("sum of all even numbers: ")
sum=0
for i in my_cars1:
    if i%2==0:
        sum+=i
print(sum)

#remove duplicate number from the list
my_cars1 = [9, 15, 10, 20, 27, 24, 66, 70, 20, 66, 10 ]
print("duplicate the same number: ")
res = [*set(my_cars1)]
print("List after removing duplicate elements: ", res)


#dictionary 
salesperson = {"manish": "6 january 1996", "rakesh":"10 febrauary 2000","pavan":"15 march 2001","naresh": "18 april 2003" }
def birthdate(name):
    print(salesperson[""+name+""])

birthdate("naresh")
