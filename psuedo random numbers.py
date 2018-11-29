y = 100
for i in range(1,11):
    x = (572 * y + 27) % 2059
    print(x)
    y = x
    
