
# MappingProxyType builds a read-only mappingproxy instance from a dict
from types import MappingProxyType

d = {1: "A"}
d_proxy = MappingProxyType(d)
d_proxy  # mappingproxy({1: 'A'})
d_proxy[1]  # A

# d_proxy[2] = 'x'  # typeerror, proxy does not support assignment

d[2] = 'B'
d_proxy  # mappingproxy({1: 'A', 2: 'B'})
d_proxy[2]  # 'B'



