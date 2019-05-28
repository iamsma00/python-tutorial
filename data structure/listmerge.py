# single line code
print([(x,y) for x in [1,2,3] for y in [2,4,5] if x!=y])

# using for loop and if statement
merge = []
for x in range(1,4):
    for y in [2,4,5]:
                 if x!=y:
                    merge.append((x,y))

print(merge) 
