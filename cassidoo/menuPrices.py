#**Given a list of menu items and their prices, and the amount in your wallet, return all combinations of items that you can buy.**

#Example:
#    menu = { 'taco' : 1, 'burger' : 2, 'shawarma' : 3 }
#    wallet = 3
#    > combo(menu, wallet)
#    ['taco', 'taco', 'taco']
#    ['taco', 'burger']
#    ['shawarma']

def combo(menu, wallet, choices, index):	
	if wallet <= 0:
		print(choices)
		return
	if wallet == len(menu):
		return
	#get the amounts first to obtain the choices
	choices.append(menu[index][0])
	print(wallet)
	combo(menu, wallet-menu[index][1], choices, index)
	del choices[-1]
	combo(menu, wallet, choices, index+1)
	
menu = [["cola", 1], ["fries", 2], ["shake", 4], ["hamburger",5]]
# h, [ffc], [fccc], [sc], [ccccc]
combo(menu, 5, [], 0)
