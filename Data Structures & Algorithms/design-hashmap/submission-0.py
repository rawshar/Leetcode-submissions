class ListNode:
    def __init__(self,key=-1,value=-1,next=None):
        self.next=next
        self.value=value
        self.key=key

class MyHashMap:

    def __init__(self):
        self.map=[ ListNode() for x in range(1000)]
        

    def put(self, key: int, value: int) -> None:
        node=self.map[key%1000]
        while node.next:
            if node.next.key==key:
                node.next.value=value
                return
            node=node.next
        node.next=ListNode(key,value)
        return
        
        

    def get(self, key: int) -> int:
        node=self.map[key%1000].next
        while node:
            if node.key==key:
                return node.value
            node=node.next
        return -1
        

    def remove(self, key: int) -> None:
        node=self.map[key%1000]
        while node.next:
            if node.next.key==key:
                node.next=node.next.next
                return

            node=node.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)