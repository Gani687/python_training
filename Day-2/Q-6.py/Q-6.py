import pkg
import datetime

f = pkg.File('.')
print(f.getMaxSize(2))
print(f.getLatestFiles(datetime.date(2025,3,8)))