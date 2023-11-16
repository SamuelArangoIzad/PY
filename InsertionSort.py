def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
lista = [11,15,18,23,30,8,5,16,1] #en este caso se puede poner la lista
#interpretrando de esta numero la lista que deseamos ordenar con datos
#desordenados
insertion_sort(lista)
print("Order: " , lista)