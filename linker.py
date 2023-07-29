sars = input()
refsars = sars +"/index.html"
a = open(refsars)
source = a.read()
a.close()