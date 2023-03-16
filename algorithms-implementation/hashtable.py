import sys

class List:
    def __init__(self, data=None, next=None):
        self.data = data;
        self.next = next;

def search_list(l, x):
    if l.data is x:
        return l
    elif l.next is None:
        return None
    else:
        return search_list(l.next, x)

# Dictionary implementation using hash function and linked list for collisions
class DictionaryHashLL:
    def __init__(self, length):
        self.length = length
        self.table = [None] * length

    # Hash function
    def _hash(self, s):
        sum = 0
        for c in s:
            sum += ord(c) * 52

        return (2 * sum + 1) % self.length

    # Given data x, insert into the hash dictionary
    def insert(self, x):
        h = self._hash(x)
        if self.table[h] is None:
            self.table[h] = List(x, None)

    # Print our hash table fully
    def print_table(self):
        index = 0
        for l in self.table:
            print(index, end=" ")
            if l != None:
                print(l.data, end=" ")
                curr = l
                while curr.next != None:
                    print(l.next.data, end=", ")
                    curr = curr.next
            print(" ")
            index += 1


l3 = List("Joe")
l2 = List("John", l3)
l1 = List("Emma", l2)

d = DictionaryHashLL(10)
d.insert('Pao')
d.insert('Sally')
d.insert('John')
d.insert('Mister')
d.insert('Jesse')
d.insert('Felix')
d.print_table()
