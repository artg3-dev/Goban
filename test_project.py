from gamerules.test import test_func

with open('sgf info.sgf') as f:
    raw = f.read()

raw = raw.replace('\n', '')
text = raw.split(';')
text = [';'  + line for line in text if line]

with open('new.txt', 'w') as f:
    f.write('\n'.join(text))
