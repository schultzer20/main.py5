def power(a, b):
    if a > 0 and b > 0:
        return a**b
    else:
        return -1


print(power(2, 7))


def binary_search(numbers, num, start, end):
    if end >= start:
        mid = (start + end) // 2  # to determine where the middle is
        if numbers[mid] == num:  # if the number we are looking for is the middle
            return mid
        elif numbers[mid] > num:  # if the number we are looking for is smaller than the middle we have to look on left
            return binary_search(numbers, num, start, mid - 1)  # function calls on itself with a new end
        elif numbers[mid] < num:  # if the number we are looking for is bigger than the middle we have to look on right
            return binary_search(numbers, num, mid + 1, end)  # function calls on itself with a new start
    else:
        return -1


numbers = [1, 2, 3, 4, 5, 6]
num = 4

print(binary_search(numbers, num, 0, len(numbers)-1))


cap = 50


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return

    def __repr__(self):
        return str(self)


class HashTable:
    def __init__(self):
        self.capacity = cap
        self.size = 0
        self.buckets = [None]*self.capacity

    def __my_hash(self, element):
        hs = 0
        for idx, c in enumerate(element):
            hs += (idx + len(element)) ** ord(c)
            hs = hs % self.capacity
        return hs

    def insert(self, element, value):
        self.size += 1
        index = self.__my_hash(element)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(element, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(element, value)

    def get_element(self, element):
        index = self.__my_hash(element)
        node = self.buckets[index]
        prev = None
        while node is not None and node.key != element:
            prev = node
            node = node.next
        if node is None:
            return False
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                self.buckets[index] = node.next
            else:
                prev.next = prev.next.next
            return element

    def get_size(self):
        pass
