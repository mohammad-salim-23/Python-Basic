# Default parameter
def sum(num1,num2,num3=0):
    result = num1+num2+num3
    return result
total=sum(12,13)
print('total',total)
#args
def all_sum(num1,num2,*numbers):
    print(numbers)
    sum=0
    for num in numbers:
        print(num)
        sum=sum+num
    return sum
total = all_sum(45,46,3,4,5,6)
print('all sum',total)#output:18
