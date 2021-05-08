#To perform addition using the '+' arithmetic operator
a=1000
b=200
c=a+b
print('The sum of a and b is:',c)
#To perform subtraction using the '-' arithmetic operator
d=a-b
print('The difference between a and b is:',d)
#to perform multiplication using the '*' arithmetic operator
e=a*b
print('The product of a and b is:',e)
#To perform division using the '/' arithmetic operator
f=a/b
print('The division result of a and b is:',f)
#To perform exponential operation using the '**' arithmetic operator
g=a**b
print('The exponential operation result of a and b is:',g)
#To perform floor operation using the '//' arithmetic operator
h=a//b
print('The floor operation result of a and b is:',h)
#To us the '<' comparison operator
i=a<b
print('Is the value of a less than the value of b?',i)
#To us the '>' comparison operator
k=a==b
print('Are the values of a and b equal?',k)
#To use the '!=' comparison operator
l=a!=b
print('Is the value of a not equal to the value of b?',l)
#To use the '<=' comparison operator
m=a<=b
print('Is the value of a less than or equal to b?',m)
#To use the '>=' comparison operator
n=a>=b
print('Is the value of a greater than or equal to b?',n)
#To use the 'and' logical operator
o=a>b and b<a
print('The result of the "and" logical operator is:',o)
#To use the 'or' logical operator
p=a>b or b>a
print('The result of the "or" logical operator is:',p)
#To use the 'not' logical operator
q=not(a>b)
print('The result of the "not" logical operator is:',q)
#To use the 'is' identity operator
r=a is b
print('The result of the 'is' identity operator is:',r)

#To use the 'is not' identity operator
s=a is not b
print('The result of the 'is not' identity operator is:', s)

#To us the 'in' membership operator
strvar = 'Earth'
t='r'in strvar
print('The result of the 'in' membership operator is:',t)

#To use the 'not in' membership operator
u='b' not in strvar
print('The result of the "not in" membership operator is:', u)

#To determine operator precedence between multiplication and addition
num=10
r=a+b*num
print('The result of the expression involving multiplication and addition is:',r)

#To determine operator precedence using paratheses in an expression
s=(a+b)*num
print('The result of the expression using paratheses is:',s)

#To determine the rule of associativity when operators with the same precedence level are used in an expression
t=(a+b)-num
print('The result of the expression using the rule of associativity is:',t)




