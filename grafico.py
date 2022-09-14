import matplotlib.pyplot as plt

x=[1,2,3]
y=[10,20,30]

plt.bar(x,y)
plt.title("plot")
plt.xticks(x,x)
plt.savefig("grafico.png")

print("grafico creato")
