def array_problems_solver():
    # Misol uchun massiv va o'zgaruvchilar
    A = [10, 20, 30, 40, 50, 60, 70, 80]
    n = len(A)
    print(f"Boshlang'ich massiv: {A}\n")

    # --- Array16 ---
    # Tartib: boshidan bitta, oxiridan bitta...
    print("Array16 natijasi:")
    res16 = []
    for i in range(n // 2):
        res16.append(A[i])
        res16.append(A[n - 1 - i])
    if n % 2 != 0:
        res16.append(A[n // 2])
    print(*res16)

    # --- Array17 ---
    # Tartib: boshidan ikkita, oxiridan ikkita...
    print("\nArray17 natijasi:")
    res17 = []
    i = 0
    j = n - 1
    while i <= j:
        # Boshidan ikkita
        res17.append(A[i])
        if i + 1 <= j:
            res17.append(A[i+1])
        i += 2
        # Oxiridan ikkita
        if i <= j:
            res17.append(A[j])
            if j - 1 >= i:
                res17.append(A[j-1])
        j -= 2
    print(*res17)

    # --- Array18 ---
    # Oxirgi elementdan kichik bo'lgan birinchi element
    print("\nArray18 natijasi:")
    found18 = 0
    last_el = A[n-1]
    for x in A:
        if x < last_el:
            found18 = x
            break
    print(found18)

    # --- Array19 ---
    # A[0] < A[k] < A[n-1] shartiga mos oxirgi element indeksi
    print("\nArray19 natijasi:")
    found19 = 0
    for k in range(n-1, -1, -1):
        if A[0] < A[k] < A[n-1]:
            found19 = k
            break
    print(found19)

    # --- Array20 ---
    # K va L indekslar orasidagi elementlar yig'indisi
    K, L = 2, 5  # Misol uchun indekslar
    print(f"\nArray20 natijasi (K={K}, L={L}):")
    if 0 <= K <= L < n:
        suma = sum(A[K:L+1])
        print(suma)
    else:
        print("Indekslar xato berilgan.")

# Dasturni ishga tushirish
array_problems_solver()