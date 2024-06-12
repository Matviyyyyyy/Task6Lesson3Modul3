from SQLAgent import SQLAgent

class COP:
    def __init__(self, db):
        self.db = SQLAgent("database.db")

    def sum_sells(self):
        return self.db.fetch_all_without_params('''
        SELECT SUM(orders.quantity * products.price) AS all_sum  
        FROM products  
        INNER JOIN orders ON products.product_id = orders.product_id;''')

    def count_orders_every_customer(self):
        return self.db.fetch_all_without_params('''
        SELECT customers.first_name, customers.last_name, COUNT(orders.quantity)  
        FROM orders  
        INNER JOIN customers ON customers.customer_id = orders.customer_id  
        GROUP BY customers.first_name;
        ''')
    def avg_check_of_order(self):
        return self.db.fetch_all_without_params('''
        SELECT orders.order_id, AVG(orders.quantity * products.price)as AVARAGE_OF_SUM  
        FROM orders  
        INNER JOIN products ON products.product_id = orders.product_id  
        GROUP BY orders.order_id;
        ''')
    def most_famous_category(self):
        return self.db.fetch_all_without_params('''
        SELECT MAX(orders.quantity), products.category  
        FROM products  
        INNER JOIN orders ON orders.product_id = products.product_id  
        GROUP BY products.category;
        ''')
    def count_products_of_category(self):
        return self.db.fetch_all_without_params('''
        SELECT SUM(orders.quantity), products.category 
        FROM orders
        INNER JOIN products ON orders.product_id = products.product_id
        GROUP BY products.category;
        ''')
    def update_price_products(self):
        self.db.execute_query_without_params('''
        UPDATE products
        SET price = price * 1.10
        WHERE category = 'Cмартфони';
        ''')