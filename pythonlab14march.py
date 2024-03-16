#wap using  class to calculate area and perimter of a square
class square:
  def area(self,l):
    self.l = l
    print("the area of square is ",self.l*self.l)
  def perimeter(self , b):
    self.b = b
    print("the perimeter of the square is ",4*self.b*self.b)
s = square()
m = int (input ("enter the side of the square"))
s.area(m)
s.perimeter(m)

class rectangle:
  def area(self,l,b):
    self.l = l
    self.b=b
    print(self.l*self.b)
r=rectangle()
r.area(10,5)

#wap using class to calculate factorial of a number
class factorial_cal:
    def calculate_factorial(self, n):
        if n < 0:
            return "Factorial is not defined for negative numbers"
        elif n == 0:
            return 1
        else:
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result


calculator = factorial_cal()
number = int(input("enter the number "))
factorial_result = calculator.calculate_factorial(number)
print(factorial_result)

class Math:
    n=0.0
    def table(self):
        print("Table")
        for i in range(1,11):
            a=i*self.n
            print(a)

    def factorial(self):
        if self.n == 0 or self.n == 1:
            print(1)
        else:
            c = 1
            for i in range(2, self.n + 1):
                c = c * i
            print("Factorial of the number: ",c)
math=Math()
math.n=2
math.table()