import sqlite3


def create():
    conn = sqlite3.connect('data/stock.db')
    print('Opened database successfully')
    c = conn.cursor()

    c.execute('''
        DROP TABLE STOCK_CODE
    ''')
    c.execute('''
        CREATE TABLE STOCK_CODE(
            S_INDEX INTEGER PRIMARY KEY AUTOINCREMENT,
            STOCK_CODE TEXT    NOT NULL,
            STOCK_NAME TEXT    NOT NULL
            )''')
    print("Table created successfully")

    conn.commit()
    conn.close()


def update():
    print("update")


def insert(items):
    conn = sqlite3.connect('data/stock.db')
    c = conn.cursor()

    for item in items:
        name = item[0]
        code = item[1]
        code_sql = "INSERT INTO STOCK_CODE VALUES (NULL, '{0}', '{1}')".format(code, name)
        c.execute(code_sql)

    print("Table created successfully")
    conn.commit()
    conn.close()


def query(items):
    conn = sqlite3.connect('data/stock.db')
    c = conn.cursor()

    text = "'" + items[0] + "'"
    if len(items) > 0:
        for i in range(1, len(items)):
            text += ", '" + items[i] + "'"

    code_sql = "SELECT * FROM STOCK_CODE WHERE STOCK_CODE.STOCK_NAME in ({0})".format(text)
    c.execute(code_sql)
    rows = c.fetchall()
    conn.commit()
    conn.close()

    result = []
    for row in rows:
        result.append(row)

    return result
