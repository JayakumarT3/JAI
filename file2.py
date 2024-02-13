# from polymorphism import *
#
# ##print(x)
# ##print(_a) #protected
# ##print(__b) #private
#
# obj = Encap()
#
# print(obj.a)
# print(obj._b)
# print(obj._Encap__c)


##
##a=100
##b=1000
##if __name__=="__main__":
##    print("hai")


def hi():
    def hello():
        return "hello"
    return hello
    
a= hi()
print(a())
