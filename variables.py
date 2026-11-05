product_name1 = "Orbital strike cannon"
product_name2 = "Hyperkinetic Chainsaw"
product_name3 = "DDR5 65GB RAM"

product_price1 = 1
product_price2 = 5
product_price3 = 9.999

product_description1 = "A powerful weapon that can destroy entire planets with a single shot."
product_description2 = "A chainsaw that can cut through anything, even metal and stone."
product_description3 = "High-performance RAM for demanding applications."

product_stock1 = 100
product_stock2 = 50
product_stock3 = 0

product_name1_sold = 100
product_name2_sold = 50
product_name3_sold = 0

total_revenue1 = product_price1 * product_name1_sold
total_revenue2 = product_price2 * product_name2_sold
total_revenue3 = product_price3 * product_name3_sold

print(f"Product: {product_name1}, Price: ${product_price1}, Description: {product_description1}, Stock: {product_stock1}, Sold: {product_name1_sold}")
print(f"Product: {product_name2}, Price: ${product_price2}, Description: {product_description2}, Stock: {product_stock2}, Sold: {product_name2_sold}")
print(f"Product: {product_name3}, Price: ${product_price3}, Description: {product_description3}, Stock: {product_stock3}, Sold: {product_name3_sold}")

print(f"Total revenue for {product_name1}: ${total_revenue1}")
print(f"Total revenue for {product_name2}: ${total_revenue2}")
print(f"Total revenue for {product_name3}: ${total_revenue3}")

print(f"Total revenue for all products: ${total_revenue1 + total_revenue2 + total_revenue3}")
