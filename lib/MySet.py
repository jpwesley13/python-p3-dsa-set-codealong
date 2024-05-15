class MySet:

    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True # The values passed into the enumerable list are stored as keys on the dictionary.

    def has(self, value):
        return value in self.dictionary # doing "return self.dictionary[value]" will return true if it exists, but will return None, not false, if it doesn't. The "in" keyword always returns ToF.
    
    def add(self, value):
        self.dictionary[value] = True # Adds the value to the Dictionary as a key.
        return self # Seems to return the set with the value added.
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self # Returns None if the value does not exist. 
    
    def size(self):
        return len(self.dictionary)
    
    