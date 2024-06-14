def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def factorial_with_stack(n):
    stack = []
    result = 1
    while n > 1:
        stack.append(n)
        n -= 1
    while stack:
        result *= stack.pop()
    return result

while True:
    print("Input 1 untuk menghitng faktorial")
    print("Input 2 untuk keluar")
    print("")
    pilih = input("Input pilihan anda : ")
    print("")
    if pilih == "1":
        number = int(input("Input nilai faltorial: "))
        print("Hasil faktorial dari", number, "menggunakan rekursi:", factorial_recursive(number))

        stack_factorial_result = 1
        for i in range(1, number + 1):
            stack_factorial_result *= i
        print("Hasil faktorial dari", number, "menggunakan stack:", stack_factorial_result)
        print("")
    elif pilih == "2":
        break
    else:
        print("PILIHAN YANG ANDA MASUKKAN KURANG TEPAT. SILAHKAN ULANGI")
        print("")