numbers = [5,10,15,20,25]; sum=0;
for num in numbers:
    print(num)
    sum=sum+num
    if sum>20:
        print('bigger values',sum)

print(sum)

# for character
text = 'pagla howa'

for char in text:
    print(char)

#range
""" range for loop er structure:
for variable in range (start,stop,step) """
for i in range(1,10,2):
    print(i)
