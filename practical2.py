# ============================================
# TWO HASHING METHODS
# ============================================

def division_hash(key, table_size):
    return key % table_size


def mid_square_hash(key, table_size):
    square = key * key
    mid = (square // 10) % table_size
    return mid


# ============================================
# HASH TABLE USING CHAINING (Division Method)
# ============================================

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    # ---------- Insert ----------
    def insert(self, key):
        index = division_hash(key, self.size)
        if key not in self.table[index]:
            self.table[index].append(key)
            print(f"{key} inserted at index {index}")
        else:
            print("Key already exists")

    # ---------- Search ----------
    def search(self, key):
        index = division_hash(key, self.size)
        if key in self.table[index]:
            print(f"{key} found at index {index}")
        else:
            print(f"{key} not found")

    # ---------- Delete ----------
    def delete(self, key):
        index = division_hash(key, self.size)
        if key in self.table[index]:
            self.table[index].remove(key)
            print(f"{key} deleted from index {index}")
        else:
            print(f"{key} not found")

    # ---------- Display ----------
    def display(self):
        print("\nHash Table:")
        for i in range(self.size):
            print(f"{i} : {self.table[i]}")


# ============================================
# MENU-DRIVEN DRIVER CODE
# ============================================

if __name__ == "__main__":
    size = int(input("Enter hash table size: "))
    ht = HashTable(size)

    while True:
        print("\n1.Insert  2.Search  3.Delete  4.Display  5.Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            key = int(input("Enter key to insert: "))
            ht.insert(key)

        elif choice == 2:
            key = int(input("Enter key to search: "))
            ht.search(key)

        elif choice == 3:
            key = int(input("Enter key to delete: "))
            ht.delete(key)

        elif choice == 4:
            ht.display()

        elif choice == 5:
            print("Exiting program...")
            break

        else:
            print("Invalid choice")
