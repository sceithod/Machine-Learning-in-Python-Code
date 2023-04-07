
import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.15
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
IT = [2.22,3.15,2.55,4,5.25,4.55,3.85,4,8,7.15]
ECE = [3.02,4,3.15,4.85,6,5.85,5.25,5.55,8.35,8]
CSE = [3.89,4.85,5,6,6.85,7.15,7,7,10,9.25]
 
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
plt.ylim(0, 13)
# Adding Xticks
#plt.xlabel('Branch', fontweight ='bold', fontsize = 15)
plt.ylabel('Stress detection overhead (KB)', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(IT))],
        ["Subject 1", "Subject 2", "Subject 3","Subject 4","Subject 5","Subject 6","Subject 7","Subject 8","Subject 9","Subject 10"],fontweight ='bold', fontsize = 10)
plt.title('Graphical representation of Stress detection overhead')
plt.legend()
plt.show()
