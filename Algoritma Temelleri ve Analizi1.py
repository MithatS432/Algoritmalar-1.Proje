def linear_search(arr, target):
    """
    Verilen dizide hedef öğeyi doğrusal olarak arar.
    Bulursa indeksini döner, bulamazsa -1 döner.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Örnek kullanım
liste = [3, 5, 7, 9, 11, 15]
hedef = 9
sonuc = linear_search(liste, hedef)

if sonuc != -1:
    print(f"{hedef} bulundu, indeks: {sonuc}")
else:
    print(f"{hedef} listede yok.")
