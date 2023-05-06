import re

ptn = r'[A-Z]'
txt = input()
print(str(re.search(ptn, txt).start()+1))
