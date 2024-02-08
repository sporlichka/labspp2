#1
def cross(n):
    for i in range(n):
        for_pr = ''
        for j in range(n):
            if j == i or j == n - i - 1:
                for_pr += '*'
            else: for_pr += ' '
        print(for_pr)
cross(9)
#2
def square(n):
    str1 = "*"*n
    print(str1)
    for i in range(n-2):
        str2 = ''
        for j in range(n):
            if j == 0 or j == n - 1:
                str2 += '*'
            else: str2 += ' '
        print(str2)
    print(str1)
square(5)
#3
class Elephant:
    def __init__(self, weight, height, age):
        self.weight = weight
        self.height = height
        self.age = age
    def set_name(self, name):
        self.name = name
    def get_name(self):
        print(self.name)
class Baby_El(Elephant):
    def __init__(self, weight, height, age, toys):
        super().__init__(weight, height, age)
        self.toys = list(toys)
    def set_friend(self, name_fr):
        self.friend = name_fr
    def get_friend(self):
        print(self.friend)
eve = Baby_El(25, 34, 2, ['Giraffe', 'bob'])
eve.set_name('wall-e')
eve.get_name()
eve.set_friend('zebra')
eve.get_friend()
