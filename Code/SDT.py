
import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.15
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
IT = [1.35,2.25,5,6.25,8,7.45,9,12,11,10]
ECE = [1.85,3,5.85,7,9.15,9,9.85,14.15,12.45,11.35]
CSE = [3,3.55,7,8.35,12,10.35,11,15,15,13]
 
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
plt.ylim(0, 17)
# Adding Xticks
#plt.xlabel('Branch', fontweight ='bold', fontsize = 15)
plt.ylabel('Stress detection time (ms)', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(IT))],
        ["Subject 1", "Subject 2", "Subject 3","Subject 4","Subject 5","Subject 6","Subject 7","Subject 8","Subject 9","Subject 10"],fontweight ='bold', fontsize = 10)
plt.title('Graphical representation of stress detection time')
plt.legend()
plt.show()
