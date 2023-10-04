import matplotlib.pyplot as plt

categories = ['Smartphones', 'TVs', 'Laptops', 'Tablets', 'Coffee machines']
items_sold = [550, 280, 450, 300, 350]

plt.figure(figsize=(8, 6))
plt.bar(categories, items_sold, color='green')

plt.xlabel('Categories')
plt.ylabel('Number of Items Sold')
plt.title('Items Sold by Category')

plt.show()
