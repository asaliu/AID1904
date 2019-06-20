import getpass
import hashlib

# 输入隐藏
pwd = getpass.getpass("PW:")
print(pwd)
# hash对象
#　算法加盐 (#$awv3) 把用户密码和这个盐（key）拼接后加密
# abc123#$awv3　拼接后加密防止逆推
# hash = hashlib.md5()  # 生成对象

hash = hashlib.md5("*#06l".encode())
hash.update(pwd.encode())  # 加密处理
pwd = hash.hexdigest()  # 提取加密后的密码
print(pwd)
