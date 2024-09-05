def insert_product_data(product_name, price, discount_percent, original_price, product_url):
    # SQL query to insert data into the products table
    query = """
    INSERT INTO products (product_name, price, discount_percent, original_price, product_url)
    VALUES (%s, %s, %s, %s, %s)
    """
    
    # Data to be inserted
    data = (product_name, price, discount_percent, original_price, product_url)
    
    # Execute the query
    cursor.execute(query, data) # type: ignore
    
    # Commit the transaction to save the data
    connection.commit() # type: ignore

    print(f"Product '{product_name}' inserted into the database.")
