import requests

<<<<<<< HEAD
res = requests.get('https://www.theverge.com/tech')
f = open('site.html', 'w')
=======
res = requests.get('https://www.theverge.com/tech') # Obtain the source of the webpage, and
f = open('site.html', 'w')                          # write it to a local file.
>>>>>>> 60aaa06be48eede974a27b9f4fd002cad6bea5c4
f.write(res.text)

def lst(string):
    ls = string.split('<')
    l = []

    for t in ls:
        for k in t.split('>'):
            l.append(k)

    return l

<<<<<<< HEAD
f = open('site.html', 'r')
=======
f = open('site.html', 'r')                         # Read and interpret the generated local file.
>>>>>>> 60aaa06be48eede974a27b9f4fd002cad6bea5c4
lines = f.readlines()
i = 0
print("\nToday's headlines from the Tech section of the website of The Verge:-\n")
for line in lines:
<<<<<<< HEAD
    if (line[:44] == '    <h2 class="c-entry-box--compact__title">'):
        i += 1
=======
    if (line[:44] == '    <h2 class="c-entry-box--compact__title">'):   # All headlines on this page follow this
        i += 1                                                          # condition in the source code.
>>>>>>> 60aaa06be48eede974a27b9f4fd002cad6bea5c4
        ls = lst(line)
        print('%d: %s' % (i, ls[len(ls) - 5]))
print('\n')
