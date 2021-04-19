class Node:
    def __init__(self, prev = None, data = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("\nLinked List is empty.")
            return

        ll_str = ""
        itr = self.head
        while itr:
            # ll_str += str(itr.data) + " --> " 
            ll_str += f"{itr.data} --> "
            itr = itr.next
        
        print("\n" + ll_str + "\n")

    def print_backward(self):
        if self.head is None:
            print("\nLinked List is empty.")
            return

        ll_str = ""
        itr = self.get_last_node()
        while itr:
            # ll_str += str(itr.data) + " --> " 
            ll_str += f"{itr.data} --> "
            itr = itr.prev
        
        print("\n" + ll_str + "\n")

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(None, data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(itr,data, None)

    def insert_start(self, data):
        if self.head is None:
            node = Node(None, data, self.head)
            self.head = node
        else:
            node = Node(None, data, self.head)
            # self.head.prev = node
            self.head = node

    def get_last_node(self):
        itr = self.head 
        while itr.next:
            itr = itr.next
        
        return itr

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("INVALID INDEX")
        
        if index == 0:
            self.insert_start(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(itr, data, itr.next)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1


    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_end(data)

    
if __name__ == "__main__":

    dll = DoubleLinkedList()

#     dll.insert_start(50)

#     dll.print_forward()
#     dll.print_backward()
    dll.insert_at(0,10)

    dll.insert_end(100)
    dll.insert_end(200)
    dll.insert_end(300)

    dll.print_forward()
    dll.insert_at(3,20)
    dll.insert_at(5,20)

    dll.remove_at(4)

    dll.print_forward()

#     dll.print_backward()
    
#     dll.insert_start(50)
#     dll.insert_start(20)

#     dll.print_forward()
#     dll.print_backward()
    
#     last = dll.get_last_node()
#     print(last.data)
    
#     ll.insert_values(["banana","mango","grapes","orange"])
#     ll.print()
    
#     ll.insert_after_value("mango","apple") # insert apple after mango
#     ll.print()

#     ll.remove_by_value("orange") # remove orange from linked list
#     ll.print()

#     ll.remove_by_value("figs")
#     ll.print()

#     ll.remove_by_value("banana")
#     ll.print()
    
#     ll.remove_by_value("mango")
#     ll.print()

#     ll.remove_by_value("apple")
#     ll.print()

#     ll.remove_by_value("grapes")
#     ll.print()
