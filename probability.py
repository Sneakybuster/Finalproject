import matplotlib.pyplot as plt

left_coordinates = []
x = int(input("How many bars do you want? "))
for i in range(1,x + 1):
    left_coordinates.append(i)
heights = []
for j in range(len(left_coordinates)):
    v = int(input("Enter heights: "))
    heights.append(v)
bar_labels = []
for k in range(x):
    bar_labels.append(k)
plt.bar(left_coordinates, heights, tick_label = bar_labels, width = 0.6, color = ['red', 'black'])
plt.xlabel('X-Axis')
plt.ylabel('Y-Label')
plt.title("This is a Bar Graph")
plt.show()

