
class node:
    def __init__(self, val=0, nxt=None, prev=None, parent_key=None):
        
        self.parent_key = parent_key
        self.val = val
        self.nxt = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        
        self.key_dict = {}
        self.max_cap = capacity
        self.lru = None
        self.mru = None
        self.cap = 0
        
        

    def get(self, key: int) -> int:
        
        #print(key)
        
        if key in self.key_dict:
            
            if self.lru != self.mru:
                
                
                
                
                curr_node = self.key_dict[key]
                
                #print(self.lru.val, curr_node.val)
                
                if self.lru == curr_node:
                    
                    
                
                    self.lru = curr_node.nxt
                    
                    

                    self.lru.prev = None

                    self.mru.nxt = curr_node
                    curr_node.prev = self.mru
                    curr_node.nxt = None
                    self.mru = curr_node
                    #print(self.mru.val)
                

                elif self.mru == curr_node:
                    
                    return self.key_dict[key].val
                    
               
                else:

                    curr_node.prev.nxt = curr_node.nxt
                    curr_node.nxt.prev = curr_node.prev

                    self.mru.nxt = curr_node
                    curr_node.prev = self.mru

                    self.mru = curr_node
                    curr_node.nxt = None
                    

            
            
            return self.key_dict[key].val
        
        else:
            return -1
        
        

    def put(self, key: int, value: int) -> None:
        
        if key not in self.key_dict:
            #print(key)
            
            new_node = node(value, None, self.mru, key)
            
            self.key_dict[key] = new_node
            
            #pointer_change
            
            if self.mru != None:
                
                self.mru.nxt = new_node
                self.mru = new_node
                
            else:
                self.mru = new_node
            
            
            if self.lru == None:
                self.lru = new_node
                
                
            self.cap += 1
            
            
            if self.cap > self.max_cap:
                #print(self.lru.val)
                self.lru.nxt.prev = None
                
                del self.key_dict[self.lru.parent_key]
                
                self.lru = self.lru.nxt
                #print(self.lru.val, "lru")
                
            
        else:
            
            
            if self.lru != self.mru:
                
                
                
                
                curr_node = self.key_dict[key]
                
                if self.lru == curr_node:
                    
                    curr_node.val = value
                
                    self.lru = curr_node.nxt

                    self.lru.prev = None

                    self.mru.nxt = curr_node
                    curr_node.prev = self.mru
                    curr_node.nxt = None
                    self.mru = curr_node
                
                elif self.mru == curr_node:
                    
                    curr_node.val = value
                    
                
                else:
                    
                    curr_node.val = value


                    curr_node.prev.nxt = curr_node.nxt
                    curr_node.nxt.prev = curr_node.prev

                    self.mru.nxt = curr_node
                    curr_node.prev = self.mru

                    self.mru = curr_node
                    curr_node.nxt = None

                    
                    


            else:
                
                curr_node = self.key_dict[key]
                curr_node.val = value
                
                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
