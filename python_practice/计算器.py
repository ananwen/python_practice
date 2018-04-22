class Calculate():

    def __checknum_zsq(func):
        def inner(self,n):
            if  not isinstance(n,int):
                raise TypeError("number is not a int")
            return func(self,n)
        return inner



    def __creat_output_zsq(word=""):
        def __output_zsq(func):
            def inner(self, n):
                print(word+"%d"%n)
                return func(self, n)
            return inner
        return __output_zsq

    def __init__(self,num):
        self.__result = num

    @__checknum_zsq
    @__creat_output_zsq("jia")
    def jia(self,n):
        self.__result += n
        return self

    @__checknum_zsq
    @__creat_output_zsq("jian")
    def jian(self,n):
        self.__result -= n
        return self
    @__checknum_zsq
    @__creat_output_zsq("cheng")
    def cheng(self,n):
        self.__result *= n
        return self

    def clear(self):
        self.__result = 0
        return self

    def show(self):
        print(self.__result)

    @property
    def result(self):
        return self.__result
c1=Calculate(1)
# c1.jia(4)
# c1.cheng(4)
# c1.show()
# print(c1.result)
c1.jia(2).jia(2).clear().show()