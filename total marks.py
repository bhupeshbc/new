s=int(input('enter marks of science:'))
m=int(input('enter marks of maths:'))
n=int(input('enter marks of nepali:'))
e=int(input('enter marks of english'))

total_marks = s+m+n+e
total_percentage = (total_marks/400)*100

print(f'the total marks of sutdennt is {total_marks}')
print(f'the percentage obtained by student is {total_percentage}')

if total_percentage>70 :
    print('your obtained distinction')
elif total_percentage>60:
    print('you obtained first division')
elif total_percentage>40:
    print('you are pass')
else:
    print('you are fail')
