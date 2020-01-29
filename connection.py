import sqlite3
import os
from operators import db_operator
file_path = os.getcwd()
db_path = file_path+'\mogo.db'


operator = db_operator(db_path,'regulations')

# operator.build()
operator.insert_db('舍那可怜的就罚款决定书离开房间啊了','煤太多了')
operator.insert_db('企鹅日期欧赔入侵我排位u人','煤太少了')

operator.find_db('煤太少了')