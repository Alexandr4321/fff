class Car:

    def __init__(self, label:str, color:str,year:int):
        self.label=label
        self.color=color
        self.year=year


    def drive(self):
        print('Bbbbrrrrrrr-rrrr-rrr')

my_car=Car('Mazda','black','2020')
new_car=Car('Mercedes','white','2023')
old_car=Car('Жигули','Коричневый','1945')
auto_park=[my_car,new_car,old_car]
