import random

class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.val_to_index:
            # Move the last element to the place of the element to delete
            last_element = self.values[-1]
            idx_to_remove = self.val_to_index[val]
            self.values[idx_to_remove] = last_element
            self.val_to_index[last_element] = idx_to_remove
            
            # Remove the last element
            self.values.pop()
            del self.val_to_index[val]
            return True
        
        return False

    def getRandom(self) -> int:
        return random.choice(self.values)
