# ============================================
# Dictionary ADT using Hash Table (Chaining)
# ============================================

class DictionaryADT:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return

    def display(self):
        print("\nDictionary Contents:")
        for bucket in self.table:
            for pair in bucket:
                print(f"{pair[0]} : {pair[1]}")


# ============================================
# DRIVER CODE WITH RANDOM SAMPLE DATA
# ============================================

if __name__ == "__main__":
    d = DictionaryADT(5)

    # Random example data
    d.insert("name", "Alice")
    d.insert("age", 21)
    d.insert("city", "Delhi")
    d.insert("course", "BTech")
    d.insert("roll_no", 105)

    d.display()

    print("\nSearch Example:")
    print("city →", d.search("city"))

    print("\nAfter Update:")
    d.insert("age", 22)
    d.display()

    print("\nAfter Delete:")
    d.delete("course")
    d.display()
