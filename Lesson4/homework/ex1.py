inventory = {'gold':500,
'pouch':['flint','twine','gemstone'],
'backpack':['xylophone','dagger','bedroll','brealoaf']
}

inventory['pocket']=0
inventory['pocket']=['seashell','strange berry','lint']

inventory['backpack'].remove('dagger')

inventory['gold']+=50

print(inventory)