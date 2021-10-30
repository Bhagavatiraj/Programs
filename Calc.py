import sys
n1 = sys.argv[1]
n1 = int(n1)

n2 = sys.argv[2]
n2 = int(n2)


print('first number: {0} '.format(n1))
print('Second number: {0} '.format(n2))

sum = float(n1) + float(n2)  
sub = float(n1) - float(n2)  
mul = float(n1) * float(n2)  
div = float(n1) / float(n2)  

print('The sum of {0} and {1} is {2}'.format(n1, n2, sum))      
print('The subtraction of {0} and {1} is {2}'.format(n1, n2, sub))  
print('The multiplication of {0} and {1} is {2}'.format(n1, n2, mul))  
print('The division of {0} and {1} is {2}'.format(n1, n2,div))
