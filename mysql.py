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
# myquery="insert into mmhk values('','Md. Mehedi Hasan Khan',21)"
# myquery="delete from mmhk where id=1"
myquery="select * from mmhk"


mydata=mycursor.execute(myquery)

results = mycursor.fetchall()
print("__ID______________Name__________________Age_")
for row in results:
    
    print("ID:",row[0],"\tName:",row[1],"\tAge:",row[2])


conn.commit()
conn.close()