
from collections import defaultdict
a = defaultdict(lambda :'N/A')
a['a'] = 1
print a['a']
print a['b']


from collections import deque
b = deque(['a', 'b'])
print b
b.append('c')
b.appendleft('d')
print b

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y']);
c = Point(3, 4)
print c, c.x, c.y
