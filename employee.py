class Employee:
    def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
            self.email = first + '.' + last + '@vybez.com'
            
emp_1 = Employee('Brianna', 'Flemings', 100000)
emp_2 = Employee('Anna', 'McBride', 100000)


emp_1.first = 'Brianna'
emp_1.last = 'Flemings'
emp_1.email = 'Briannaflemings@vybez.com'
emp_1.pay = 100000


emp_2.first = 'Anna'
emp_2.last = 'McBride'
emp_2.email = 'test@vybez.com'
emp_2.pay = 100000


print (emp_1.email)
print (emp_2.email)


