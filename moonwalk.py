def MoonWalk(CR,CC,TR,TC):
if CR > TR or CC > TC:
return 0
if CR == TR and CC == TC:
return 1
return(MoonWalk(CR,CC+1,TR,TC) + MoonWalk(CR+1,CC,TR,TC))
# get the input (range)
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
print(MoonWalk(0,0,rows-1,columns-1))
