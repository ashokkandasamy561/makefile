import matplotlib.pyplot as plt
month =[1,2,3,4,5,6,7,8,9]
sale = [100,170,140,100,100,150,190,165,1200]
plt.bar(month,sale)
plt.title("microcontroller sales data")
plt.xlabel("month number")
plt.ylabel("sales units in number")
plt.grid(linestyle = "--")
plt.tight_layout()
plt.show()

