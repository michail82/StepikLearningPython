x = int( input() )
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print( 'Високосный' )
else:
    print( 'Обычный' )

print( 2000 % 400 )
# print (1992400)
# print (1900//400)
