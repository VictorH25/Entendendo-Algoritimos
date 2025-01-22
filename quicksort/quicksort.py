def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array [0]
        menores = [i for i in array [1:] if i <= pivo]
        maiores = [i for i in array [1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)
print (quicksort([10,5,2,3,9,8,1,4,6,7]))

5 / 3 / 1 / 2 / 4
1/ 5 / 3 / 2 / 4
1 / 2 / 3 / 5 / 4
1/ 2 / 3 / 4 / 5