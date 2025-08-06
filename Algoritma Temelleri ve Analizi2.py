def selection_sort(arr):
    """
    Seçmeli sıralama algoritmasıyla diziyi sıralar.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # En küçük elemanla yer değiştir
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Örnek kullanım
liste = [64, 25, 12, 22, 11]
print("Sıralanmadan önce:", liste)
selection_sort(liste)
print("Sıralandıktan sonra:", liste)
