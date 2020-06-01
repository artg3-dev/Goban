import re
regex = re.compile(r"(.*)(<class ')(.*)('>)(.*)")

with open('sgf_properties.py') as f:
    raw = f.read()

split_by_line = raw.split('\n')
cleaned = []

for line in split_by_line:
    mo = regex.search(line)
    try:
        result = mo.groups()
    except:
        cleaned.append(line)
    else:
        new_line = result[0] + ' ' + result[2] + result[4]
        cleaned.append(new_line)

with open('new.py', 'w') as f:
    f.write('\n'.join(cleaned))