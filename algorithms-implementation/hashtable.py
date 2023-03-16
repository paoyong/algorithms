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
    def __init__(self, size):
        self.length = size

# Hash function
def hash(x):
    return (2 * x + 1) % 10

def main(argv):
    print(hash(int(argv[0])))

    l3 = List("Joe")
    l2 = List("John", l3)
    l1 = List("Emma", l2)

    print(search_list(l1, "John").data)


if __name__ == "__main__":
   main(sys.argv[1:])

