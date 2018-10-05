class X(Y): 创建一个叫Ｘ的类，他是Ｙ的一种
class X(object):def __init__ (self,J):　类Ｘ有一个__init__,他接受self和J作为参数
class X(object):def M(self,J):类Ｘ有一个名为Ｍ的函数，他接受self和J作为参数
foo = X():将foo设为Ｘ的一个实例
foo.M(J):从foo中找到M函数，并使用self　和　J参数调用它
foo.K = Q:从foo中获取Ｋ属性，并将其设为Q
