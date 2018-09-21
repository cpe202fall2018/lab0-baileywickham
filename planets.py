def weight_on_planets():
   # write your code here
   a = int(input("What do you weigh on earth? "))
   print("\nOn Mars you would weigh {m} pounds.\nOn Jupiter you would weigh {j} pounds.".format(m=a*.38, j=a*2.34))
   
   
if __name__ == '__main__':
   weight_on_planets()
