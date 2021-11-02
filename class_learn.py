class Person:
#类里面定义的函数叫做方法，和函数的区别是，方法的第一个参数都是self，起到指代的作用
    def __init__(self,name,sex,birthday): #初始化方法,也叫构造方法，self后其他的参数都是从外面传进来的，self是自己
        self.name = name
        self.sex = sex
        self.birthday = birthday #将来是要传参进来的，注意参数是传到类里
    def say(self,word): #定义类的通用方法
        print(f'{self.name}说："{word}"')

zhangsan = Person('张三','male','20020202')
zhangsan.say('你好')
