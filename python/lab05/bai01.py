import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=.; DATABASE=QLMonAn; UID=sa; PWD=sa; Encrypt=no')
cursor = conn.cursor()
cursor.execute("SELECT @@version")
# conn.close()
db_version = cursor.fetchone()
print("Bạn dùng hệ quản trị CSDL SQL sever phiên bản", db_version)

# import sqlite3

# def get_connection():
#     connection = sqlite3.connect('QlSinhVien.db')
#     return connection

# def close_connection(connection):
#     if connection:
#         connection.close()

# def read_database_version():
#     try:
#         connection = get.connection()
#         cursor = connection.cursor()
#         cursor.execute("select sqlite_version();")
#         db_version = cursor.fetchone()
#         print("Bạn đang sử dụng SQLite phiên bản:", db_version)
#         close_connection(connection)
#     except (Exception, sqlite3.Error) as error:
#         print("Đã có lỗi xảy ra. Thông tin lỗi: ", error)

# read_database_version()

