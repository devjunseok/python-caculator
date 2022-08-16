
class divClass:
    def div(self, val1, val2):
        return val1 /val2

class calculator(divClass): 
    
   
    def sum(self, val1, val2): 
        self.val4 = val1+val2
        return self.val4

cal = calculator()
print(cal.sum(3,4))

