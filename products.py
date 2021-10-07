# -------------------------------------------------
# Load some data 
def load_data(path):
	list = []
	with open(path, 'r') as data:
		for line in data: 
			info = line.split(',')
			list.append(info)

	return list

# Get the list of products
products = load_data('./products.txt')

# --------------------------------------------------
def login(food):
	# Search products and match food
	for user in products:
		if food.lower() in user[1].lower():
			# Find a match and return it as a dictionary
			return {
				'food': user[1],
				'price': float(user[2]),
                'count': float(user[3]),
                'total': float(user[3])*float(user[2])
			}
		
	# If nothing is found return a dictionary with an error 
	return {
		'error': 'Item not found'
	}
# ----------------------------------------------------

# Display messsage 
def displayUser(user):
	# Check for an error
	if 'error' in user:
		# Display the error
		print(user["error"])
		return

	# Display the user
	print(f'Name: {user["food"]}, price: {user["price"]}, count: {user["count"]}, total: {user["total"]}')

# -----------------------------------------------------

answer='yes'
while answer=='yes':
    # Prompt for user food
    food = input('Enter food: ')
    # Call login and get the results
    result = login(food)
    # Display the results
    displayUser(result)
    # Prompt if the user wants to search again
    answer= input("Would you like to search again?(yes/no)")
    if answer=='yes':
        answer=='yes'
    else:
        print('Have a good day!')
        answer=='no'
