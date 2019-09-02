import numpy as np
import matplotlib.pyplot as plt

file_path = 'training_data_xsub.txt'

mean_loss1 = []
mean_loss_class = []
mean_loss_recon = []
Eval_mean_loss1 = []
Eval_mean_loss_class = []
Eval_mean_loss_recon = []
Top1 = []
Top5 = []

with open(file_path, 'r') as f:
    line = f.readline()
    while line:
        if line.find('\tmean_loss1: ') >= 0:
            mean_loss1.append(float(line[line.find('mean_loss1: ')+12:line.find('\n')]))
        elif line.find('\tmean_loss_class: ') >= 0:
            mean_loss_class.append(float(line[line.find('mean_loss_class: ')+17:line.find('\n')]))
        elif line.find('\tmean_loss_recon: ') >= 0:
            mean_loss_recon.append(float(line[line.find('mean_loss_recon: ')+17:line.find('\n')]))
        elif line.find('\tEval_mean_loss1: ') >= 0:
            Eval_mean_loss1.append(float(line[line.find('Eval_mean_loss1: ')+17:line.find('\n')]))
        elif line.find('\tEval_mean_loss_class: ') >= 0:
            Eval_mean_loss_class.append(float(line[line.find('Eval_mean_loss_class: ')+22:line.find('\n')]))
        elif line.find('\tEval_mean_loss_recon: ') >= 0:
            Eval_mean_loss_recon.append(float(line[line.find('Eval_mean_loss_recon: ')+22:line.find('\n')]))
        elif line.find('\tTop1: ') >= 0:
            Top1.append(float(line[line.find('Top1: ')+6:line.find('%')]))
        elif line.find('\tTop5: ') >= 0:
            Top5.append(float(line[line.find('Top5: ')+6:line.find('%')]))
        line = f.readline()

x1 = range(11, 101)
x2 = range(15, 101, 5)

plt.subplot(3, 1, 1)
plt.plot(x1, mean_loss_class, 'o-', label = 'Training Set')
plt.plot(x2, Eval_mean_loss_class, 'o-', label = 'Validation Set')
plt.title('AS-GCN xsub: Recognition loss on Train/Val vs. epoches')
plt.xlabel('epoches')
plt.ylabel('loss')
plt.legend(loc = 'upper right')

plt.subplot(3, 1, 2)
plt.plot(x1, mean_loss_recon, 'o-', label = 'Training Set')
plt.plot(x2, Eval_mean_loss_recon, 'o-', label = 'Validation Set')
plt.title('AS-GCN xsub: Prediction loss on Train vs. epoches')
plt.xlabel('epoches')
plt.ylabel('loss')
plt.legend(loc = 'right')

plt.subplot(3, 1, 3)
plt.plot(x2, Top1, 'o-', label = 'Top1 accuracy')
plt.plot(x2, Top5, 'o-', label = 'Top5 accuracy')
plt.title('AS-GCN xsub: Top1 & Top5 accuracy on Val')
plt.xlabel('epoches')
plt.ylabel('Accuracy (%)')
plt.legend(loc = 'right')
plt.annotate('best Top1 accuracy: 84.52%', xy=(x2[13],Top1[13]), \
             xytext=(x2[13]-20,Top1[13]-6),arrowprops=dict(arrowstyle='->'))
plt.annotate('best Top5 accuracy: 96.83%', xy=(x2[13],Top5[13]), \
             xytext=(x2[13]-20,Top1[13]+8),arrowprops=dict(arrowstyle='->'))
plt.annotate('84.15% here, paper reported 86.8% on 100th epoch', xy=(x2[17],Top1[17]), \
             xytext=(x2[13]-10,Top1[13]+3),arrowprops=dict(arrowstyle='->'))

# plt.subplots_adjust(wspace = 0, hspace = 1)

fig = plt.gcf()
fig.set_size_inches(10,20)

plt.savefig('ASGCN_loss.png', dpi=200)
plt.show()
