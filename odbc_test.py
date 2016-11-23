import pypyodbc  
  
  
Config = {  
          'dsn':'test_db_XP',   
          }  
  
conn = pypyodbc.connect("DSN=test_db_XP;UID=sa;pwd=")  
cur = conn.cursor()  
  
  
cur.execute(''''' 
            select * from t_test1 
        ''')  
  
  
  
cur.execute(''''' 
            create table dbo.t_test(id int) 
         ''')  
cur.commit()  
  
cur.execute(''''' 
            insert into t_test(id) values(1) 
        ''')  
  
cur.commit()  

#解决其实很简单，在connect方法加入autocommit=True就行了。
