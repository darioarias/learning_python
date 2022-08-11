from collections import namedtuple
from bisect import bisect, insort




# list.sort, sorts the list in place
PQ_Item = namedtuple('PQ_Item', 'data priority')
def sorter(item: PQ_Item):
  return item.priority

pq_list = [PQ_Item('Pepe', 3), PQ_Item('Amen', 2), PQ_Item('Rica', 1)]
pq_list.sort(key=sorter)


num_list = [1, 2, 3, 4, 5, 6]

# num_list[bisect(num_list, 2):bisect(num_list, 2)] = [2]
insort(num_list, 2)





