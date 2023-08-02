import os

name = input('Enter Name: ')
owner = input('Enter owner name: ')

# Create the directory if it does not exist
if not os.path.exists(name):
    os.makedirs(name)
else:
    print(f'Sorry , this domain is claimed by annother person. Check out the \'owndet\' afile in the directory for {name}')

refname = os.path.join(name, "index.html")
create = open(refname, "w")  # Change "x" to "w" for write mode
create.write(
f'''
<!DOCTYPE html>
<html>
<head>
    <title>{name}</title>
</head>
<body>
    <h1 align="center">Welcome to {name}! This site was created with web.com's START program. Visit start.web.com for more details. This site is owned by {owner}. If you would like to use this domain, contact them. If this site hasn't been updated ever, contact web.com.</h1>
</body>
</html>
''')
create.close()
