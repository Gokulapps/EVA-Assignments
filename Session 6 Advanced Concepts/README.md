In this Folder, I have Uploaded Three Python Files and one Notebook File. My Target was to take Cifar10 Dataset and desgin an Neural Network which will attain an 
Validation Accuracy of 85% in as many epochs as possible. Initially I created a Model.py File in which i designed a Neural Network with 1,97,000 Parameters. I have attached the Architecture and Summmary of the Model is below, 

![image](https://user-images.githubusercontent.com/61132761/217616302-c0fda28d-b878-41d0-8adc-3773a25e537d.png)

As a Next Step I created a augmentation.py File where i Implemented Augmentation Strategies like Cutout, Horizontal Flip and Shift Scale Rotate using Albumentation 
Library. This File takes Batch of Images as an Input and Returns Augmented Image. There is a seperate Python File for Training and Testing the Network on a given
Input. I basically created two functions named train and test which would take Inputs like Model, Dataset, Optimizer and other Necessary Stuffs to Train and Validate 
the Network. Then there is one Python File for all the Utility Functions like Plotting Model's Accuracy Graph and Loss Graph, Plotting Ten Misclassified Images of the 
Model, Visualizing the Input Images. 

On Top of all this I have created a Notebook File where all the Functions are Implemented by Importing all these Python files. I have Displayed the Training Logs,
the Augmented Images, Plots for Model's Loss and Accuracy. In these File I was able to achieve Toplidation Accuracy of 79.73 at 36th Epoch for the Cifar10 Dataset.
I have attached short clipped Training Logs below, 

EPOCH: 30
Loss=1.0715317726135254 Batch_id=12499 Accuracy=75.43

Test set: Average loss: 0.1552, Accuracy: 7871/10000 (78.71%)

EPOCH: 31
Loss=0.9638179540634155 Batch_id=12499 Accuracy=76.71

Test set: Average loss: 0.1500, Accuracy: 7952/10000 (79.52%)

EPOCH: 32
Loss=0.6767711639404297 Batch_id=12499 Accuracy=77.18

Test set: Average loss: 0.1498, Accuracy: 7929/10000 (79.29%)

EPOCH: 33
Loss=0.7482537627220154 Batch_id=12499 Accuracy=77.28

Test set: Average loss: 0.1488, Accuracy: 7930/10000 (79.30%)

EPOCH: 34
Loss=0.7177951335906982 Batch_id=12499 Accuracy=77.16

Test set: Average loss: 0.1491, Accuracy: 7961/10000 (79.61%)

EPOCH: 35
Loss=0.5878340601921082 Batch_id=12499 Accuracy=77.27

Test set: Average loss: 0.1490, Accuracy: 7963/10000 (79.63%)

EPOCH: 36
Loss=0.8210248947143555 Batch_id=12499 Accuracy=77.43

Test set: Average loss: 0.1484, Accuracy: 7973/10000 (79.73%)

EPOCH: 37
Loss=1.1308162212371826 Batch_id=12499 Accuracy=77.43

Test set: Average loss: 0.1487, Accuracy: 7953/10000 (79.53%)

EPOCH: 38
Loss=0.9188569188117981 Batch_id=12499 Accuracy=77.46

Test set: Average loss: 0.1489, Accuracy: 7947/10000 (79.47%)

EPOCH: 39
Loss=1.2761874198913574 Batch_id=12499 Accuracy=77.48

Test set: Average loss: 0.1485, Accuracy: 7966/10000 (79.66%)

EPOCH: 40
Loss=1.4156683683395386 Batch_id=12499 Accuracy=77.43

Test set: Average loss: 0.1486, Accuracy: 7954/10000 (79.54%)

The Plot for Network's Accuracy and Loss is shown below, 

![image](https://user-images.githubusercontent.com/61132761/217615664-c02a364c-3ace-4357-97c6-1810a7fdf302.png)

Ten Misclassified Images by the Network is shown below to Understand the shortcomings of the Model

![image](https://user-images.githubusercontent.com/61132761/217615940-a0549575-a47a-40c2-bb2a-d06b3b928d58.png)
