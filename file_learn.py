f = open('文档名称',encoding='utf-8') #这里的参数要加上编码
s = read(f) #读取文件内容
print(s) #输出文件内容
f.close() #最终要把文件关闭