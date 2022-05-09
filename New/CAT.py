class Cat(object):
    def __init__(self, color, cat_type: str):
        self.size = ''
        self.color = color
        self.cat_type = cat_type

    def set_size(self):
        if self.cat_type == 'indoor':
            self.size = 'small'
        else:
            self.size = 'undefined'
        return self.size


mr_cat = Cat('black', 'indoor')
mr_cat.set_size()
print(mr_cat.size)


class Tiger(Cat):
    __weight = 18

    def set_size(self):
        if self.cat_type == 'wild':
            self.size = 'big'
        else:
            self.size = 'undefined'
        return self.size


mr_big = Tiger('black', 'wild')
mr_big.set_size()
print(mr_big.size)
