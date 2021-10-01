conn = sqlite3.connect('lab55.db')
print("Opened succesfully")
conn.execute('''CREATE TABLE employees
            (EMPNO INT PRIMARY KEY   NOT NULL,
             ENAME   CHAR(30)    NOT NULL,
             JOB  CHAR(20)    NOT NULL,
             SAL  REAL(20)    NOT NULL,
             HIREDAT CHAR(50)    NOT NULL);''')
print("Table created successfully")
