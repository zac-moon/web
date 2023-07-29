def main():
    site = input('Enter Site to launch : ')
    ref = site + "/index.html"
    domref = site + '/'

    s = open(ref)
    source = s.read()
    s.close()

main()