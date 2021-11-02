# author：魏慧敏
# 学习时间：2021/10/2610:31 下午
a = 10 #变量存储的是一个对象的引用，即指向内存空间
lst1 = [10,200,300,10,80,90,100]
#print(id(list)) #输出列表的id
#print(type(list)) #输出列表的类型
#print(lst1) #输出列表的值
#print(lst1[0]) #输出列表的第一个值
#print(lst1.index(10))  #当存在多个重复的数据时，索引返回第一个数据的索引
#print(lst1.index('hello',1,3)) #指定范围1，3中查找hello的索引
#print(lst1[1:6:1])  #切片操作，start=1,stop=4,step=1 注意这里切出来的应该是hello和where，因为是不包括3的，另，我们默认步长是1
#print(lst1[1:6:2])  #start=1,stop=6,step=2
#print(lst1[::-1]) #从后往前输出列表中的值
#print(10 in lst1) #判断10是否在列表中，是输出true，否输出false
'''判断可迭代变量是否在列表中，是的话输出元素中各个值
for item in lst1:
    print(item)
'''
''' #append方法的使用
print(lst1)
lst1.append(200)  
print('添加之后的列表是：',lst1)
'''
'''extend方法的使用
lst2 = ['hello','world']
lst1.extend(lst2)
print(lst1)
'''
'''insert方法的使用
lst1.insert(1,90)
print(lst1)
'''
'''列表的切片操作，也可以作为增加来使用，即切掉的部分用什么来替代
lst3 = ['we','are','girls']
lst1[1:] = lst3 #从索引为1的位置开始切片，后面的都替换为lst3
print(lst1)
'''
'''remove方法：删除列表中的一个指定元素
print(lst1)
lst1.remove(10) #移除列表中的元素，如果有重复元素，只移除第一个
print(lst1)
'''
'''pop方法：删除指定索引的元素
print(lst1)
lst1.pop(1) #删除索引为1的元素
print(lst1)
'''
'''pop没有参数的情况
print(lst1)
lst1.pop()
print(lst1)
'''
'''切片操作
print(lst1)
lst2 = lst1[1:3]
print(lst2)
'''
'''删除多个元素且不生成新的列表对象
print(lst1)
lst1[1:3]=[]
print(lst1)
'''
'''clear清空列表中的所有元素
print(lst1)
lst1.clear()
print(lst1)
'''
'''del直接删除整个列表对象
del lst1
print(lst1)
'''
'''直接修改列表中的一个元素
print(lst1)
lst1[1] = '你好'
print(lst1)
'''
'''
print(lst1)
lst1[1:3]=['pro','iphone',90,100]
print(lst1)
'''
'''sort（）方法进行升序排序
print(lst1)
lst1.sort()
print(lst1)
'''
'''指定reverse参数对列表进行降序排序
print(lst1)
lst1.sort(reverse=True)
print(lst1)
'''
'''使用内置函数sorted对列表元素进行排序
print(lst1)
sorted(lst1)
print(lst1)
'''
'''列表生成式，产生从1到10到数据
lst2 = [i for i in range(1,10)]
print(lst2)
'''
'''列表生成式，生成2，4，6，8，10数据
lst2 = [i*2 for i in range(1,6)]
print(lst2)
'''
print(lst1)












#第二种创建列表的方式
#lst2 = list(['今天',100,200])
#print(lst2)

