import pastset

my_list = [1, 2, 3]

pset = pastset.PastSet()
test = pset.enter(('Test', list, int))
test.move((my_list, 42, 43, 44))
print test.first(), test.last()
print test.observe()
print test.first(), test.last()

pset.halt()

