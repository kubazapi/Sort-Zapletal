import random
array = [88,45,1,23,8,74,23,36,99,6]

def bubble_sort():     # Definice funkce `bubble_sort`, která třídí seznam metodou bubble_sort.
    n = len(array)            # Zjišťuje délku pole , které chceme seřadit.
    for i in range(n-1):      # První smyčka se provádí n-1 krát
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :    # Porovnává aktuální prvek a následující prvek.
                array[j], array[j+1] = array[j+1], array[j]  # Pokud je aktuální prvek větší než následující, zamění je.
            print(array)  # Vypisuje stav pole po každé změně.
    return array         #Vrací setříděné pole.
print(bubble_sort())      #Volá funkci `bubble_sort` a vypisuje její výstup.

def is_sorted(array):       # Definice funkce `is_sorted`, která kontroluje, zda je seznam seřazený.
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:     # Porovnává aktuální prvek s předchozím.
            return False              # Vrátí False, pokud seznam není seřazený.
    return True                   # Pokud se smyčka dokončí, znamená to, že seznam je seřazený.

def bogosort(array):  # Definice funkce `bogosort`, která třídí seznam metodou bogosort.
    count = 0
    while not is_sorted(array):          # Smyčka se provádí, dokud seznam není seřazený.
        random.shuffle(array)         # Náhodně promíchá pořadí prvků v seznamu.
        count += 1                    # Zvýší počitadlo pokusů o 1.
        print(f"Pokus {count}: {array}")   # Vypíše aktuální počet pokusů a stav seznamu po promíchání.
    print(f"Seznam seřazen po {count} pokusech.")   # Když je seznam seřazený, vypíše, po kolika pokusech se to podařilo.

bogosort(array)    # Volá funkci `bogosort` s proměnnou `array`.
print("Seřazený seznam:", array) # Vypíše finální seřazený seznam.

def selection_sort(array):   # Definice funkce `selection_sort`, která třídí seznam metodou selection_sort.
    n = len(array)           # Zjistí délku seznamu, který má být seřazen.
    for i in range(n):       # Pro každý prvek seznamu spustí vnější smyčku, která postupně zajišťuje správné umístění prvků.
        min_i = i  
        for j in range(i + 1, n):          # Prochází zbytek seznamu a hledá skutečně nejmenší prvek.
            if array[j] < array[min_i]:      # Porovnává prvek na indexu `j` s aktuálním nejmenším.
                min_i = j  
        array[i], array[min_i] = array[min_i], array[i]  # Zamění hodnoty mezi aktuální pozicí a pozicí nalezeného nejmenšího prvku.
    return array     # Vrátí seřazený seznam.

selection_sort(array)                  # Zavolá funkci `selection_sort` s proměnnou `array`.
print("Seřazený seznam:", array)       # Vypíše finální seřazený seznam.

def insertion_sort(array):             # Definice funkce `insertion_sort`, která třídí seznam metodou insertion_sort.
    for i in range(1, len(array)):     # Smyčka začíná od druhého prvku a prochází seznam. První prvek je považován za "setříděný".
        key = array[i]                 # Ukládá aktuální prvek jako "klíč", který bude vložen na správné místo.
        j = i - 1                          # Přesune se na předchozí prvek.
        while j >= 0 and key < array[j]:   # Posouvá prvky v setříděné části seznamu, které jsou větší než "klíč", o jedno místo doprava.
            array[j + 1] = array[j]        # Posun aktuálního prvku doprava.
            j -= 1                         # Přesune se na předchozí prvek.
        array[j + 1] = key                 # Vloží "klíč" na správnou pozici.
    return array             # Vrátí seřazený seznam.

insertion_sort(array)            # Zavolá funkci `insertion_sort` s proměnnou `array`.
print("Seřazený seznam:", array) # Vypíše finální seřazený seznam.
