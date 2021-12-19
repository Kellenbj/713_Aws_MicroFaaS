import random
from datetime import datetime
import string

start = datetime.now()
x = ""
for _ in range(4):
    x=x.join(random.choices(string.ascii_letters + string.digits, k=64))
    random.randint(1,10000)

end = datetime.now()

diff = end-start
ex = diff.total_seconds()*1000

print("Total ex time:", ex, "ms")

