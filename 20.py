conn = sqlite3.connect('lab56.db')
print("Opened succesfully")
conn.execute('''CREATE TABLE customers1
            (EMPNO INT PRIMARY KEY   NOT NULL,
             ENAME   CHAR(30)    NOT NULL,
             AGE REAL(10)    NOT NULL,
             ADDRESS  CHAR(50)    NOT NULL,
             SAL  REAL(20)    NOT NULL);''')
print("Table created successfully")
