class Kangaroo(object):
    def __init__(self, n):
        self.pouchcontents = []
        self.name = n

    def __str__(self):
        s = self.name + ' :' + str(self.pouchcontents)
        return s

    def put_in_pouch(self, item):
        self.pouchcontents.append(item)


kanga = Kangaroo('kanga')
roo = Kangaroo('roo')
kanga.put_in_pouch('food')
roo.put_in_pouch('more food')
roo.put_in_pouch("chicken")
print(kanga)
print(roo)
