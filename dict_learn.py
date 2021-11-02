# author：魏慧敏
# 学习时间：2021/10/305:50 下午

'''使用{}方式创建字典
scores = {'huimin':100,'aa':35}
print(scores)
print(type(scores))
'''
'''使用dict函数进行字典的创建
zhangsan = dict(name='zhangsan',age='20')
print(zhangsan)
print(type(zhangsan))
'''
'''空字典的创建
d = {}
print(d)
'''
d = {'name':'jack','age':20,'zhangsan':100}
print(d)

#print(d['name'])  使用字典对象[key]的方式获取字典的值
'''get函数来获取字典中的值
print(d.get('name'))
print(d.get('sex','hello'))
'''
# print('name' in d) 判断name是否在字典中
'''字典元素的删除，使用del语句，传入key进行删除
del d['zhangsan']
print(d)
'''
'''字典元素的清空
d.clear()
print(d)
'''
'''直接增加一个没有的key和值即可
d['王五']=200
print(d)
'''
'''对给定的key进行修改
d['zhangsan']=200
print(d)
'''
'''获取字典中所有的key
keys = d.keys()
print(keys)
print(list(keys))
'''
'''获取字典中所有的value
values = d.values()
print(values)
print(list(values))
'''
'''输出字典所有的键值对
items = d.items()
print(items)
print(list(items)) #转换以后的元素是元组
'''
'''遍历字典元素
for item in d:
    print(item,d.get(item))
'''
lst1 = ['age1','age2','age3']
lst2 = [10,20,30]
d = {age.upper():num for age,num in zip(lst1,lst2)}
print(d)



















