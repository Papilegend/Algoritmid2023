def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Tagastab indeksi, kui element on leitud
    return -1  # Tagastab -1, kui elementi pole leitud

# Näide kasutamisest
minu_list = [2, 5, 8, 12, 16, 23, 38, 42, 50]
otsitav_element = 16

tulemus = linear_search(minu_list, otsitav_element)

if tulemus != -1:
    print(f"{otsitav_element} leiti indeksilt {tulemus}.")
else:
    print(f"{otsitav_element} ei leitud listist.")
