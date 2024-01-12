class HashTable:
    def __init__(self, m, t):
        self.m = m
        self.type = t

    def hash_1(self, k):
        return k % self.m

    def hash_2(self, k):
        if self.m == 1:
            return (k % (self.m + 1)) + 1
        else:
            return (k % (self.m - 1)) + 1

    def hash_function(self, k, i) -> int:
        if self.type == 1:
            return self.hash_1(k)
        elif self.type == 2:
            return (self.hash_1(k) + i) % self.m
        elif self.type == 3:
            return (self.hash_1(k) + i + i ** 2) % self.m
        elif self.type == 4:
            return (self.hash_1(k) + i * self.hash_2(k)) % self.m

    def insert(self, table, k):
        i = 0
        while i != self.m:
            j = self.hash_function(k, i)
            if table[j] is None:
                table[j] = k
                return j
            else:
                i += 1

    def delete(self, table, k):
        i = 0
        j = self.hash_function(k, i)
        if table[j] is None:
            return
        for i, l in enumerate(table):
            if table[i] == k:
                table[i] = 'Deleted'
                return
        return

    def search(self, table, k):
        i = 0
        j = self.hash_function(k, i)
        while table[j] is not None and i != self.m:
            j = self.hash_function(k, i)
            if table[j] == k:
                return j
            i += 1
        return None

    def chained_insert(self, table, k):
        i = 0
        j = self.hash_function(k, i)
        if table[j] is None:
            table[j] = k
        elif isinstance(table[j], list):
            table[j].insert(0, k)
        else:
            table[j] = [k, table[j]]

    def chained_delete(self, table, k):
        i = 0
        j = self.hash_function(k, i)
        if table[j] is None:
            return
        elif isinstance(table[j], list):
            if k in table[j]:
                table[j].remove(k)
                if len(table[j]) == 1:
                    table[j] = int(table[j][0])
        else:
            if table[j] == k:
                table[j] = None

    def chained_search(self, table, k):
        i = 0
        j = self.hash_function(k, i)
        if table[j] is None:
            return
        elif isinstance(table[j], list):
            for i, x in enumerate(table[j]):
                if table[j][i] == k:
                    return j
        else:
            if table[j] == k:
                return j
        return None

    def size(self):
        return self.m


def main():
    values = [int(x) for x in input().split()]
    hash_table = HashTable(values[0], values[1])
    if values[1] == 1:
        hashes = {i: None for i in range(values[0])}
        for x in values[2:]:
            hash_table.chained_insert(hashes, x)
    else:
        hashes = {i: None for i in range(values[0])}
        for x in values[2:]:
            hash_table.insert(hashes, x)
    items = list(hashes.values())
    print(items)

    while True:
        function_list = [int(f) for f in input().split()]
        if function_list[0] == -1:
            break
        elif function_list[0] == 0:
            if values[1] == 1:
                hash_table.chained_insert(hashes, function_list[1])
            else:
                hash_table.insert(hashes, function_list[1])
            items = list(hashes.values())
            print(items)
        elif function_list[0] == 1:
            if values[1] == 1:
                print(hash_table.chained_search(hashes, function_list[1]))
            else:
                print(hash_table.search(hashes, function_list[1]))
        elif function_list[0] == 2:
            if values[1] == 1:
                hash_table.chained_delete(hashes, function_list[1])
            else:
                hash_table.delete(hashes, function_list[1])
            items = list(hashes.values())
            print(items)


if __name__ == "__main__":
    main()
