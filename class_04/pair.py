x = [1,2,3]
y = [3,1,4]

comb = [(x_i,y_i) for (x_i,y_i) in zip(x,y) if(x_i!=y_i)]
print(comb)