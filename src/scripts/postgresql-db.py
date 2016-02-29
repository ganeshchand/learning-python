# conn = psycopg2.connect(connection)
# cursor = conn.cursor()
# items = pickle.load(open(pickle_file,"rb"))
#
# for item in items:
#     city = item[0]
#     price = item[1]
#     info = item[2]
#
#     query =  "INSERT INTO items (info, city, price) VALUES (%s, %s, %s);"
#     data = (info, city, price)
#
#     cursor.execute(query, data)