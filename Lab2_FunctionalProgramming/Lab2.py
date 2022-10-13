# Note the pattern: (lambda parameters : expression) (*argv)
result = (lambda x, y : x + y) (2, 3)
print(result) ; print('')

# save a lambda fxn into a variable!!!
# notice that we do not use the function definition!
sum = lambda x, y : x + y
result = sum (4, 3)
print(result)
