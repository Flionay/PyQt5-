import sqlite3
import sys

class db_operator():


    def __init__(self,dbpath,tablename):
        self.table_name = tablename
        self.dbpath = dbpath



    def build(self):
        con = sqlite3.connect(self.dbpath)
        # 获取cursor对象
        cur = con.cursor()
        # 执行sql创建表
        sql = 'create table {}(ID INTEGER PRIMARY KEY  AUTOINCREMENT ,regulation TEXT NOT NULL ,matter TEXT )'.format(self.table_name)
        try:
            cur.execute(sql)
        except Exception as e:
            print(e)
            print('创建表失败')
        finally:
            # 关闭游标
            cur.close()
            # 关闭连接
            con.close()

    def connection(self):
        con = sqlite3.connect(self.dbpath)
        cur = con.cursor()

        return cur,con



    def insert_db(self,regulations,matters):
        cur,con = self.connection()
        sql = 'insert into {}(regulation,matter) values(?,?)'.format(self.table_name)
        try:
            cur.execute(sql,(regulations,matters))
            #提交事务
            con.commit()
            print('插入成功')
        except Exception as e:
            print(e)
            print('插入失败')
            con.rollback()
        finally:
            sql = 'delete from regulations where ID not in (select max(ID) from regulations group by matter)'
            cur.execute(sql)
            con.commit()
            # 关闭游标
            cur.close()
            # 关闭连接
            con.close()


    def find_db(self,matters):
        cur, con = self.connection()

        sql = "select regulation from {} where matter like '%{}%'".format(self.table_name,matters)
        try:
            cur.execute(sql)
            # 获取所有数据
            person_all = cur.fetchall()

            # 遍历
            # for p in person_all:
            #     print(p)

        except Exception as e:
            print(e)
            print('查询失败')
        finally:
            # 关闭游标
            cur.close()
            # 关闭连接
            con.close()
            return person_all

    def find_db1(self,matters):
        cur, con = self.connection()

        sql = "select regulation from {} where matter = '{}'".format(self.table_name,matters)
        try:
            cur.execute(sql)
            # 获取所有数据
            person_all = cur.fetchall()

            # 遍历
            for p in person_all:
                print(p)

        except Exception as e:
            print(e)
            print('查询失败')
        finally:
            # 关闭游标
            cur.close()
            # 关闭连接
            con.close()
            return person_all

    def update_db(self,matters,regulations):
        cur, con = self.connection()
        try:
            # 执行sql创建表
            update_sql = "update {} set regulation = '{}' where  matter = '{}'".format(self.table_name,regulations,matters)
            #print(update_sql)
            cur.execute(update_sql)
            # 提交事务
            con.commit()
            print('修改成功')
        except Exception as e:
            print(e)
            print('修改失败')
            con.rollback()
        finally:
            sql = 'delete from regulations where ID not in (select max(ID) from regulations group by matter)'
            cur.execute(sql)
            con.commit()
            # 关闭游标
            cur.close()
            # 关闭连接
            con.close()



    def delete_db(self,matters):
        cur, con = self.connection()
        # 执行sql创建表
        delete_sql = "delete from {} where matter = '{}'".format(self.table_name,matters)
        # print(delete_sql)
        try:
            cur.execute(delete_sql)
            # 提交事务
            con.commit()
            print('删除成功')
        except Exception as e:
            print(e)
            print('删除失败')
            con.rollback()
        finally:
            # 关闭游标
            cur.close()
            # 关闭连接
            con.close()


