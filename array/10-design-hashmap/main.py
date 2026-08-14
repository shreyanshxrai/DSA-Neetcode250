class ListNode:
    def __init__(self, key, value):
        self.key = key 
        self.value = value
        self.next = None
        
class MyHashMap(object):

    def __init__(self):
        self.set = [ListNode(0,0) for i in range(10**4)]

    def put(self, key, value):
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next.value= value
                return
            cur =cur.next
        cur.next = ListNode(key , value)       
        
        

    def get(self, key):
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return cur.next.value   
            cur =cur.next
        return -1

    def remove(self, key):
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return   
            cur =cur.next