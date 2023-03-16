import sys

class List:
    def __init__(self, data=None, next=None):
        self.data = data;
        self.next = next;

    # Push onto the end of the Linked List
    def push(self, x):
        # Traverse until the end
        curr = self
        while curr.next != None:
            curr = curr.next
        curr.next = List(x)
    
    # Given data value x, traverse the linked list until found x or return None
    def search(self, x):
        curr = self

        if curr.data is x:
            return curr

        while curr.next != None:
            curr = curr.next
            if curr.data is x:
                return curr

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
        
        # If hashed into empty spot in array, initialize Linked List
        if self.table[h] is None:
            self.table[h] = List(x, None)
        # Otherwise add onto existing Linked List
        else:
            self.table[h].push(x)

    # Given a data x, return a List if exists. O(n+m)
    def search(self, x):
        for l in self.table:
            if l != None:
                ll_search_result = l.search(x)
                if ll_search_result != None:
                    return ll_search_result
        return None


    # Print our hash table fully
    def print_table(self):
        index = 0
        for l in self.table:
            if l != None:
                print(index, end=" ")
                print(l.data, end="")

                # Traverse through our linked list
                curr = l
                while curr.next != None:
                    print(", ", end="")
                    curr = curr.next
                    print(curr.data, end="")
                print(" ")
            index += 1

l3 = List("Joe")
l2 = List("John", l3)
l1 = List("Emma", l2)

d = DictionaryHashLL(100000)
d.insert('Pao')
d.insert('Sally')
d.insert('John')
d.insert('Mister')
d.insert('Jesse')
d.insert('Felix')
d.insert('Sam')
d.insert('Adept')
d.print_table()
print(d.search('Adept').data)
