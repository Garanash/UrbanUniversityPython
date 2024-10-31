import sqlite3


def initiate_db():
    conn = sqlite3.connect('Products2.db')
    c = conn.cursor()

    # Удаляем таблицу Products, если она уже существует
    c.execute('DROP TABLE IF EXISTS Products')

    # Создаем таблицу Products
    c.execute('''CREATE TABLE IF NOT EXISTS Products
                 (id INTEGER PRIMARY KEY,
                 title TEXT NOT NULL,
                 description TEXT,
                 price INTEGER NOT NULL,
                 image TEXT NOT NULL)''')

    # Добавляем данные в таблицу Products
    products = [
        (1, 'Белокочанная капуста', 'Капуста белокочанная в дополнительном представлении не нуждается', 100,
         "for_14_3/1.jpg"),
        (2, 'Баклажаны', 'Баклажан известен в обиходе под забавным прозвищем "синенький"', 200, "for_14_3/2.jpg"),
        (3, 'Картофель', 'Храним в своих погребах и кушаем по мере необходимости в течение года', 300,
         "for_14_3/3.jpg"),
        (4, 'Сладкий перец', 'Редкий овощ может похвастаться столь широким набором витаминов и микроэлементов', 400,
         "for_14_3/4.jpg")
    ]
    c.executemany('INSERT INTO Products VALUES (?, ?, ?, ?, ?)', products)

    # Удаляем таблицу Users, если она уже существует
    c.execute('DROP TABLE IF EXISTS Users')

    # Создаем таблицу Users, если она еще не создана
    c.execute('''CREATE TABLE IF NOT EXISTS Users
                 (id INTEGER PRIMARY KEY,
                 username TEXT NOT NULL,
                 email TEXT NOT NULL,
                 age INTEGER NOT NULL,
                 balance INTEGER NOT NULL)''')

    conn.commit()
    conn.close()


def add_user(username, email, age):
    conn = sqlite3.connect('Products2.db')
    c = conn.cursor()

    # Баланс по умолчанию 1000
    balance = 1000
    c.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
              (username, email, age, balance))

    conn.commit()
    conn.close()


def is_included(username):
    conn = sqlite3.connect('Products2.db')
    c = conn.cursor()

    # Проверяем наличие пользователя
    c.execute('SELECT 1 FROM Users WHERE username = ?', (username,))
    result = c.fetchone()

    conn.close()
    return result is not None


def get_all_products():
    conn = sqlite3.connect('Products2.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Products")
    products = c.fetchall()
    conn.close()
    return products
