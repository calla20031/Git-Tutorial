def multiplication_table():
    for i in range(1,10):
        for j in range(2,6):
            print(f'{j}x{i} ={j*i:2d}',end="    ")
        print()
    print()
    for i in range(1,10):
        for j in range(6,10):
            print(f'{j}x{i} ={j*i:2d}',end="    ")
        print()
        
multiplication_table()
