def quicksort(arr):
   if len(arr) <= 1: return arr
   m = arr[0]
   return quicksort([i for i in arr if i < m]) + \
          [i for i in arr if i == m] + \
          quicksort([i for i in arr if i > m])

listaUsr = [4,2,6,3,7,9,0,8,5,1]

print("Lista desordenada: ",listaUsr)

listaUsr = quicksort(listaUsr)

print("Lista ordenada: ",listaUsr)
