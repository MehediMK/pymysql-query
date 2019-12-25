import pymysql

conn=pymysql.connect(host="localhost",user="root",password="",db="mehedi")

mycursor = conn.cursor()

# myquery = """
#     create table mmhk(
#         id int AUTO_INCREMENT primary key,
#         name varchar(30),
#         age int(3) 
# )"""
# myquery="drop table mmhk"
myquery="insert into mmhk values('','Md. Mehedi Hasan Khan',21)"
# myquery="delete from mmhk where id=1"

mycursor.execute(myquery)

conn.commit()
conn.close()