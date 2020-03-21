import requests

res = requests.get('https://www.theverge.com/tech')
f = open('site.html', 'w')
f.write(res.text)

def lst(string):
    ls = string.split('<')
    l = []

    for t in ls:
        for k in t.split('>'):
            l.append(k)

    return l

f = open('site.html', 'r')
lines = f.readlines()
i = 0
print("\nToday's headlines from the Tech section of the website of The Verge:-\n")
for line in lines:
    if (line[:44] == '    <h2 class="c-entry-box--compact__title">'):
        i += 1
        ls = lst(line)
        print('%d: %s' % (i, ls[len(ls) - 5]))
print('\n')
