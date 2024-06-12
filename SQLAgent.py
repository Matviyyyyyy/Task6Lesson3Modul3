import sqlite3

class SQLAgent:
    def __init__(self, name_db):
        self.db = sqlite3.connect(name_db)
        self.create_table_products()
        self.create_table_customers()
        self.create_table_orders()

    def create_table_products(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products(      
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,      
            name TEXT NOT NULL,      
            category TEXT NOT NULL,      
            price REAL NOT NULL  ); 
        ''')
        cursor.close()

    def create_table_customers(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (   
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,    
            first_name TEXT NOT NULL,    
            last_name TEXT NOT NULL,    
            email TEXT NOT NULL UNIQUE  );
        ''')
        cursor.close()

    def create_table_orders(self):
        cursor = self.db.cursor()
        cursor.execute('''  
            CREATE TABLE IF NOT EXISTS orders (   
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,    
            customer_id INTEGER NOT NULL,    
            product_id INTEGER NOT NULL,    
            quantity INTEGER NOT NULL,    
            order_date DATE NOT NULL,    
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id),    
            FOREIGN KEY (product_id) REFERENCES products(product_id) );    

        ''')
        cursor.close()
        self.db.commit()

    def execute_query(self, query, params=()):
        cursor = self.db.cursor()
        cursor.execute(query, params)
        cursor.close()
        self.db.commit()

    def fetch_all(self, query, params=()):
        cursor = self.db.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result

    def fetch_one(self, query, params=()):
        cursor = self.db.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        return result

    def fetch_all_without_params(self, query):
        cursor = self.db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def execute_query_without_params(self, query):
        cursor = self.db.cursor()
        cursor.execute(query)
        cursor.close()
        self.db.commit()

    def save_changes(self):
        self.db.commit()

    def discard_changes(self):
        self.db.rollback()


