class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
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

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        if self.head == None:
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next 

    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head == None:
            return
        
        if self.head.data == data:
            self.head = self.head.next 
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next 

if __name__ == "__main__":

    ll = LinkedList()

    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()

    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()

    ll.remove_by_value("figs")
    ll.print()

    ll.remove_by_value("banana")
    ll.print()
    
    ll.remove_by_value("mango")
    ll.print()

    ll.remove_by_value("apple")
    ll.print()

    ll.remove_by_value("grapes")
    ll.print()

# def insert_list(head, ls):
#     itr = head 
#     for data in ls:
#         itr.data = data
#         itr = itr.next
#     return head  
        
# def reverse(head):
#     ls = []
#     itr = head 
#     while itr:
#         ls.append(itr.data)
#         itr = itr.next
#     ls.reverse()
#     head = insert_list(head, ls)

#     itr = head 
#     while itr:
#         print(itr.data)
#         itr = itr.next


# def reverse(head):
#     ls = []
#     itr = head 
#     while itr:
#         ls.append(itr.data)
#         itr = itr.next
#     ls.reverse()
#     head = insert_list(head, ls)
#     return head
