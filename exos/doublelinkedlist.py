'''
Double Linked List
In a doubly linked list, each element has the property that if element A has a "before" link to element B, then element B has an "after" link to element A
Provide a definition for an insert function that will create an ordered doubly linked list. This function is defined outside of the class Frob, and takes two arguments: a Frob that is currently part of a doubly linked list, and a new Frob. The new Frob will not initially have any "before" or "after" links to other Frobs. The function should mutate the list to place the new Frob in the correct location, with the resulting doubly linked list having appropriate "before" and "after" links.
Note that if a Frob is inserted with the same name as a pre-existing Frob, both names should be inserted in the final data structure (the exact ordering of the two identical Frobs does not matter)
From MIT CS 101 online class. 
'''

class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    
    def setBefore(self, frob):
        self.before = frob
        
    def getBefore(self):
        return self.before
    
    def setAfter(self, frob):
        self.after = frob
        
    def getAfter(self):
        return self.after
        
    def myName(self):
        return self.name
        
    def __repr__(self):
        return self.myName()

   

def insert(element, new_frog):
    b, a = findPosition(element, new_frog)
    reorder_list(b, new_frog, a)
    
f1 = Frob('hello1')
f2 = Frob('hello2')
insert(f1, f2)
print f1.getAfter()