mat_row,mat_col=map(int,input().split())
l1t=[]
for _ in range(mat_row):
    con.append(input())
for ic in range(len(con)):
    if('0' in con[ic]):
        con[ic]=con[ic].replace('0','')
    con[ic]=con[ic].replace(' ','')
lengths=[]
for ic in con:
    if(len(ic)>0):
        lengths.append(len(ic))
mat_col=min(lengths)
rt1='1 '*mat_col
rt1=rt1.strip()
for ic in range(mat_col):
    print(rt1)
