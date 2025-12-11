# ejemplo
# nums = [5, 3, 8, 4, 21, 1, 9, 2];



nums = [5, 3, 8, 4, 21, 1, 9, 2]
ordenado = []


j = True

while j:

    for e in nums:
        o= min(nums)
        ordenado.append(o)
        nums.remove(o)
        if  not nums:
            j= False

print(ordenado)