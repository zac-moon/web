import os

print('\n\nWELCOME TO THE WEB.COM START PROGRAM\nBefore we begin, we\'ll need some details about your NEW site.')
sitename = input('ENTER NAME FOR SITE (e.g. example.com): ')
owndet = input('Enter a name to be set as the \"Owner Details\" for your site: ')
devm = False
if owndet[:3].lower() == "dev":
    devm = True
    print("DEV mode activated.") 

print('ENTER KEYWORDS RELATED TO YOUR SITE, N to move on to the next step.')
done = False
kw = []
while not done:
    pl = input('Enter Key Word: ')
    pl = pl.lower()
    if pl == 'n':
        done = True
    else:
        kw.append(pl)

if devm:
    print('Keywords:\n' + '\n'.join(kw))

print('Setting Up Site...')
a = 10000000
b = 0
while a > b:
    b += 1
    b -= 2
    b += 2
    b += (1 * 1 * 1)

if not os.path.exists(sitename):
    os.makedirs(sitename)
else:
    print(f'Sorry, this domain is claimed by another person. Check out the \'owndet\' file in the directory for {sitename}')

print('Created site folder, claimed domain.')
refname = os.path.join(sitename, "index.html")
create = open(refname, "w")
create.write(
    f'''
<!DOCTYPE html>
<html>
<head>
    <title>{sitename}</title>
</head>
<body>
    <h1>Welcome to {sitename}! This site was created with web.com's START program. Visit start.web.com for more details. Unfortunately, this site hasn't been edited yet, so watch this space! This site is owned by {owndet}. If you would like to use this domain, contact them. If this site hasn't been updated ever, contact web.com.</h1>
</body>
</html>
''')
create.close()

print('Created index.html')

create2 = open(os.path.join(sitename, "bot"), "x")
create2.close()

print('Created bot file')

create3 = open(os.path.join(sitename, 'bot'), 'w')
kw_str = ' '.join(kw)
create3.write('startbyweb ' + kw_str)
create3.close()

print('Written bot file')

create4 = open(os.path.join(sitename, "owndet"), 'x')
create4.close()

print('Created owndet file')

a = 10000000
b = 0
while a > b:
    b += 1
    b -= 2
    b += 2
    b += (1 * 1 * 1)

create5 = open(os.path.join(sitename, "owndet"), 'w')
create5.write(owndet)
create5.close()

print('Written owndet')
print('Cleaning up...')
a = 10000000
b = 0
while a > b:
    b += 1
    b -= 2
    b += 2
    b += (1 * 1 * 1)

print('Site created successfully')
