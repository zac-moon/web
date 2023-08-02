print('\n\nWELCOME TO THE WEB.COM START PROGRAM\nBefore we begin, we\'ll need some details about your NEW site.')
sitename = input('ENTER NAME FOR SITE (e.g. example.com) : ')
owndet = input('Enter a name to be set as the \"Owner Details\" for your site : ')
devm = False
if owndet[:3].lower() == "dev":
    devm = True
    print("DEV mode activated.") 

print('ENTER KEYWORDS RELATED TO YOUR SITE , N to move on to the next step.')
done = False
kw = []
while not done:
    pl = input('Enter Key Word : ')
    pl = pl.lower()
    if pl == 'n':
        done = True
    else:
        kw.append(pl)

if devm:
    print('Keywords: \n' + '\n'.join(kw))

'''
subdy = input('DO you want subdomains? Y for yes and N for no: ')
'''

print('Setting Up Site...')
