tablero=[None]*8
for i in range(0,8):
    tablero[i]=[None]*8

for i in range(0,8):
    for j in range (0,8):

        if(j ==1 or j==6):
            tablero[i][j] ="P"
        
        elif((i== 0 or i==7) and (j ==0 or j==7)):
            tablero[i][j] ="t"

        elif((i== 1 or i==6) and (j ==0 or j==7)):
            tablero[i][j] ="C"

        elif((i== 2 or i==5) and (j ==0 or j==7)):
            tablero[i][j] ="A"

        elif(i== 3  and (j ==0 or j==7)):
            tablero[i][j] ="D"

        elif(i== 4  and (j ==0 or j==7)):
            tablero[i][j] ="R"

print(tablero)