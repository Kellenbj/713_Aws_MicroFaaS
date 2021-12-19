import random
from datetime import datetime
import string

start = datetime.now()
x = ""
for _ in range(1000):
    x = x.join(str(random.randint(1,128)))

end = datetime.now()

diff = end-start
ex = diff.total_seconds()*1000

print("Total ex time:", ex, "ms")

