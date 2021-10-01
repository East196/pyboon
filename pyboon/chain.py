

class Chain:
    items = []

    def __init__(self,into):
        if isinstance(into,list):
            self.items = into

    @classmethod
    def chain(cls,into):
        return Chain(into)
    


    def map(self,func):
        items = map(func,self.items)
        return Chain(list(items))

    def to_list(self):
        return self.items

    def first(self):
        return self.items[0] if self.items else None