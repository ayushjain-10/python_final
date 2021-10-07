# Product Search

Your goal is to write a program that loads the product data and searches the data for a product. 

You should load product.txt. This file is arranged in rows of data. Each row looks like this: 

```
988,Strawberries,2.46,60
```
If you split this row on the `,` (comma) you will get a list that looks like this: 

```
"988,Strawberries,2.46,60".split(',') # ['988', 'Strawberries', '2.46', '60\n']
```

Your program should do the following: 

- Prompt for a search string
- Look at each item in the list and see if the search string is _in_ the product name. 
- If it finds the item it should print the name followed by the price, the number of units, and the total cost (units * price)

For example: 

```
Search: Strawberries # PROMPT
Name: Strawberries price: 2.46 count: 60.0 total: 147.6 # DISPLAY
```

This displays total as `147.6` because the number of units 60 times the price of 2.46 per unit is 147.6.

or 

```
Search: Tea # PROMPT
Name: Snapple Raspberry Tea price: 2.41 count: 6.0 total: 14.46 # DISPLAY
```

Here we found "Snapple Raspberry Tea" because "Tea" is in the name!

If an item is not found your program should print a message saying: item not found. For example: 

```
Search: loaf # PROMPT
Item not found # DISPLAY
```

## Requirements 

You should write a program that solves the problem presented above. 

Your solution should use at least three functions to solve the problem. At least one of the functions should take one or more parameters and return a value. Here are some suggestions: 

- `load_data(path)` - this function takes the path to products.txt and returns an array of products. 
- `display_product(name, price, units)` - this function takes the name, price, and units of a product and returns a formatted string. 
- `search(str)` - takes a string, might return a formatted string.

## Stretch Goals 

If you have completed all of the problems above try these problems. 

### Search case insensitive

Currently, the search method is case-sensitive. Searching for: "Straw" should find "Strawberries" but search for "straw" will not find anything. 

Goal: Make search case insensitive. 

### Search Again

After a search prompt something like: `search again? (yes/no):`. If the input is `yes` run the search function again to prompt for a new search term. 

For example: 

```
Search: Straw # PROMPT
Name: Strawberries price: 2.46 count: 60.0 total: 147.6 # DISPLAY
Search again (yes/no):yes # PROMPT
```

### Display multiple

The product list contains a few names where a search term will overlap. For example, Cheese appears twice. The goal of this challenge is to display all entries in the product list that match a search term. 

For example: 

```
Search: Cheese # PROMPT
Name: Cheese - Brie price: 2.12 count: 17 total: 36.04 # DISPLAY
Name: "Cheese - Romano, Grated" price: 4.21 count: 85 total: 357.85 # DISPLAY
```

### Add new items to inventory

Add a new item to the inventory. 

Goal: Write a function that will take in the name, price, and number of units for a new item and add that to the inventory.

You can solve this in one of two ways. In memory in an array of products, or by appending the new item to the end of the file.

You'll need to prompt us to input the name, price, and number of units. Collect the information and then call your function. 

### Update inventory

Update the inventory. Imagine something was sold we need to update the unit count in the inventory. 

Goal: Write a function that takes the name of an item and a number of units. It should find the item in the inventory, check that the input number is equal to or less than the number of units in the inventory. If so subtract the number from the units and update the data. If not it should print an error saying "not enough units in stock". 

