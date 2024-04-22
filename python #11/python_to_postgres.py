import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'Phonebook'
username = 'postgres'
pwd = 'postgres'
port_id = 5432
conn = None
cur = None

try:
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)
    
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    
    cur.execute('DROP TABLE IF EXISTS Phonebook')
    
    create_script = ''' CREATE TABLE Phonebook (
        id  int PRIMARY KEY,
        first_name  varchar(40) NOT NULL,
        last_name  varchar(40) NOT NULL,
        phone varchar(40) NOT NULL)'''
    cur.execute(create_script)

    insert_script = 'INSERT INTO Phonebook (id, first_name, last_name, phone) VALUES (%s, %s, %s, %s)'
    insert_value = [(1, 'John', 'Johnes', '+78219245622'), (2, 'Arsen', 'Yamal', '+77777777777'), (3, 'Jack', 'Bizzly', '+78219846212'), (4, 'John', 'Keran', '+78256471125')]
    for record in insert_value:
        cur.execute(insert_script, record)

    '''update_script = 'UPDATE Phonebook SET phone = %s WHERE first_name =%s' 
    update_value = ('+78451226489', 'Arsen')
    cur.execute(update_script, update_value)
    '''

    '''cur.execute('SELECT * FROM Phonebook LIMIT 2')'''

    '''delete_script = 'DELETE FROM Phonebook WHERE first_name = %s'
    delete_value = ('Arsen',)
    cur.execute(delete_script,delete_value)'''

    cur.execute('SELECT * FROM Phonebook')
    for record in cur.fetchall():
        print(record)

    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
