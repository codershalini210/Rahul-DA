data =[[12,25,11],
        [11,14,17],
        [10,25,36]]
# data=[[00,01,02],
#       [10,11,12],
#         [20,21,22]]
# col1=data[0][0]+ data[1][0]+data[2][0]
# col2=data[0][1]+data[1][1]+data[2][1]
# col3=data[0][2]+data[1][2]+data[2][2]
# for c in range(len(data[0])):   
#     colsum=0
#     for r in range(len(data)):   
#         colsum=colsum + data[r][c] 
#     print(colsum)
# 00  10   20
# 10  11   12
# 20 21 22

for r in data:
    rsum = 0 
    for v in r:
        rsum = rsum+v
    print(rsum)