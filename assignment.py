# read an integer i< n print i^2
# using loop
n = int(input("enter the number of elements"))
for i in range(n):
    print(i * i)
# making list as user input
n = int(input("enter the number of elements"))
a = list(map(int, input("Enter the numbers : ").split()))[:n]
# square of a numbers
print(list(map(lambda num: num * num, a)))



# filter even numbers
print(list(filter(lambda num: num % 2 == 0, a)))
# filter odd numbers
print(list(filter(lambda num: num % 2 != 0, a)))
# filter age group above 18
print(list(filter(lambda num: num > 18, a)))
# prime numbers


# zip
name = ('rohit', 'kohli', 'rahul', 'suryakumar yadav')
runs = ('150', '128', '110', '88')
avg = ("60.22", '80.11', '60.55', '40.12')
print(list(zip(name, runs, avg)))
