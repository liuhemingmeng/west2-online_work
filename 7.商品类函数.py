class Commodity:
    def __init__(self,num,na,p,t,l):
        self.__number=num
        self.__name=na
        self.__price=p
        self.__total_quantity=t
        self.__left_quantity=l
    
    def display(self):
        print('商品序号：%d\n商品名称：%s\n单价：%d\n总数量：%d\n剩余数量：%d'\
              %(self.__number,self.__name,self.__price,self.__total_quantity,self.__left_quantity))
    
    def setdate(self,num,na,p,t,l):
        income=(self.__total_quantity-self.__left_quantity)*self.__price
        print('已售出商品价值i%d'%(income))
        self.__number=num
        self.__name=na
        self.__price=p
        self.__total_quantity=t
        self.__left_quantity=l