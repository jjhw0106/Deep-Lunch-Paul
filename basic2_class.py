# 클래스의 self
# 메소드는 method(self,a,b,...)에서 보듯 첫 번째 인자는 self로 되며 자동으로 들어간다. self는 다른 이름으로 명명 가능
# 여기서 self는 메소드를 호출한 객체가 된다.
# 객체 생성 후 ex.add()형식으로 호출할 경우 self를 생략해 주어야 하며, 
# ExampleClass.add의 형태로 호출 시, self 자리에 반드시 생성된 객체 ex를 명시 해주어야 한다.

class ExampleClass:
    """
    예제 클래스
    """
    def __init__(self, argument1, argument2):
        self.argument1 = argument1
        self.argument2 = argument2
    def add(self, argument1, argument2):
        """덧셈 메소드"""
        return argument1 + argument2
    def add2(self):
        """덧셈2"""
        return self.argument1 + self.argument2


ex = ExampleClass(1,3)
print(ex.add(1,3))
print(ExampleClass.add(ex,1,3))

# 클래스 상속
# 클래스(상속받을클래스)로 선언
class ChildClass(ExampleClass):
    pass

temp = ChildClass(1, 3)
print(temp.add2())

# 클래스 변수와 객체 변수
# 클래스 변수는 해당 클래스로 생성된 모든 객체가 공유하는 변수이다
# 만약에 객체 변수(self.variable)이 동일한 변수명을 사용한다면,
# 객체.argument1은 self.argument1을 가리키게 되지만,
# 클래스.argument1은 argument1을 가리키게 된다.
# 즉 argument1(클래스 변수) - self.argument1(객체 변수)는 따로 존재
class ExampleClass2:
    """클래스 변수와 객체 변수 체크용 클래스"""
    argument1 = 1
    argument2 = 2
    def __init__(self, argument3, argument4):
        self.argument1 = argument3
        self.argument2 = argument4

exA = ExampleClass2(3,4)
print(exA.argument1, exA.argument2)
print(ExampleClass2.argument1, ExampleClass2.argument2)

# __main__ 사용하기
# __name__ => 자기자신 / '__main__' => 프로그램의 시작점 
# if __name__ == '__main__': => 현재 이 파일이 프로그램의 시작점일 경우 실행해라
# import하는 경우, import 받은 파일을 실행시키면 import된 프로그램의 명령도 실행됨. 이를 방지하기 위해 __main__사용