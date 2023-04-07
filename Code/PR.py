
import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.15
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
IT = [0.86,0.9,0.9,0.95]
ECE = [0.81,0.85,0.86,0.9]
CSE = [0.77,0.8,0.81,0.85]
 
# Set position of bar on X axis
br1 = np.arange(len(IT))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
 
# Make the plot
plt.bar(br1, IT, color ='r', width = barWidth,
        edgecolor ='grey', label ='KST-NMMP')
plt.bar(br2, ECE, color ='g', width = barWidth,
        edgecolor ='grey', label ='SDCAN')
plt.bar(br3, CSE, color ='b', width = barWidth,
        edgecolor ='grey', label ='stress detection with deep learning')
plt.ylim(0, 1.3)
# Adding Xticks
#plt.xlabel('Branch', fontweight ='bold', fontsize = 15)
#plt.ylabel('Students passed', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(IT))],
        ["With preprocessing-Precision", "With preprocessing-Recall", "Without preprocessing-Precision","Without preprocessing-Recall"],fontweight ='bold', fontsize = 10)
plt.title('Graphical representations of precision and recall')
plt.legend()
plt.show()
