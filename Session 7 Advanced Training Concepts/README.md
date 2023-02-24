# Session 7 Assignment 
To create a Repo which must have files to Train the Models. Once the Repo is created, Import the Repo to the current notebook and Train Resnet18 
Model on CIFAR10 Dataset for 20 Epochs. Then Plot 10 or 20 Misclassified Images along with their GradCAM Output.  

# Repo Link 
https://github.com/Gokulapps/Pytorch-Model-Training-Base-Repo

# Training Logs 

EPOCH: 1
Loss=1.2648496627807617 Batch_id=781 Accuracy=44.80: 100%|██████████| 782/782 [00:40<00:00, 19.23it/s]

Test set: Average loss: 0.0181, Accuracy: 5808/10000 (58.08%)

EPOCH: 2
Loss=1.7595443725585938 Batch_id=781 Accuracy=60.16: 100%|██████████| 782/782 [00:40<00:00, 19.33it/s]

Test set: Average loss: 0.0151, Accuracy: 6648/10000 (66.48%)

EPOCH: 3
Loss=0.7098796367645264 Batch_id=781 Accuracy=68.02: 100%|██████████| 782/782 [00:40<00:00, 19.26it/s]

Test set: Average loss: 0.0136, Accuracy: 6952/10000 (69.52%)

EPOCH: 4
Loss=1.1286371946334839 Batch_id=781 Accuracy=72.41: 100%|██████████| 782/782 [00:40<00:00, 19.31it/s] 

Test set: Average loss: 0.0117, Accuracy: 7368/10000 (73.68%)

EPOCH: 5
Loss=0.6857098937034607 Batch_id=781 Accuracy=75.30: 100%|██████████| 782/782 [00:40<00:00, 19.20it/s] 

Test set: Average loss: 0.0103, Accuracy: 7742/10000 (77.42%)

EPOCH: 6
Loss=0.6359890103340149 Batch_id=781 Accuracy=80.94: 100%|██████████| 782/782 [00:40<00:00, 19.12it/s] 

Test set: Average loss: 0.0082, Accuracy: 8157/10000 (81.57%)

EPOCH: 7
Loss=0.614098846912384 Batch_id=781 Accuracy=81.95: 100%|██████████| 782/782 [00:41<00:00, 18.98it/s]  

Test set: Average loss: 0.0081, Accuracy: 8174/10000 (81.74%)

EPOCH: 8
Loss=0.5138347744941711 Batch_id=781 Accuracy=82.62: 100%|██████████| 782/782 [00:41<00:00, 18.81it/s] 

Test set: Average loss: 0.0079, Accuracy: 8214/10000 (82.14%)

EPOCH: 9
Loss=0.6757030487060547 Batch_id=781 Accuracy=83.16: 100%|██████████| 782/782 [00:40<00:00, 19.26it/s] 

Test set: Average loss: 0.0079, Accuracy: 8228/10000 (82.28%)

EPOCH: 10
Loss=0.6884741187095642 Batch_id=781 Accuracy=83.57: 100%|██████████| 782/782 [00:40<00:00, 19.22it/s] 

Test set: Average loss: 0.0078, Accuracy: 8261/10000 (82.61%)

EPOCH: 11
Loss=0.4095805585384369 Batch_id=781 Accuracy=84.57: 100%|██████████| 782/782 [00:40<00:00, 19.24it/s] 

Test set: Average loss: 0.0077, Accuracy: 8284/10000 (82.84%)

EPOCH: 12
Loss=0.42813757061958313 Batch_id=781 Accuracy=84.50: 100%|██████████| 782/782 [00:40<00:00, 19.26it/s]

Test set: Average loss: 0.0077, Accuracy: 8280/10000 (82.80%)

EPOCH: 13
Loss=0.6663950681686401 Batch_id=781 Accuracy=84.74: 100%|██████████| 782/782 [00:40<00:00, 19.08it/s] 

Test set: Average loss: 0.0077, Accuracy: 8304/10000 (83.04%)

EPOCH: 14
Loss=0.34011736512184143 Batch_id=781 Accuracy=84.84: 100%|██████████| 782/782 [00:40<00:00, 19.30it/s]

Test set: Average loss: 0.0077, Accuracy: 8303/10000 (83.03%)

EPOCH: 15
Loss=0.8080442547798157 Batch_id=781 Accuracy=84.76: 100%|██████████| 782/782 [00:40<00:00, 19.27it/s] 

Test set: Average loss: 0.0077, Accuracy: 8295/10000 (82.95%)

EPOCH: 16
Loss=0.8504104614257812 Batch_id=781 Accuracy=84.82: 100%|██████████| 782/782 [00:40<00:00, 19.14it/s] 

Test set: Average loss: 0.0076, Accuracy: 8304/10000 (83.04%)

EPOCH: 17
Loss=0.7786763906478882 Batch_id=781 Accuracy=84.89: 100%|██████████| 782/782 [00:41<00:00, 18.93it/s] 

Test set: Average loss: 0.0077, Accuracy: 8298/10000 (82.98%)

EPOCH: 18
Loss=0.3970058560371399 Batch_id=781 Accuracy=84.88: 100%|██████████| 782/782 [00:41<00:00, 18.91it/s] 

Test set: Average loss: 0.0076, Accuracy: 8294/10000 (82.94%)

EPOCH: 19
Loss=0.5521684885025024 Batch_id=781 Accuracy=85.18: 100%|██████████| 782/782 [00:41<00:00, 18.93it/s] 

Test set: Average loss: 0.0076, Accuracy: 8296/10000 (82.96%)

EPOCH: 20
Loss=0.6807354688644409 Batch_id=781 Accuracy=84.91: 100%|██████████| 782/782 [00:40<00:00, 19.23it/s] 

Test set: Average loss: 0.0076, Accuracy: 8305/10000 (83.05%)

# Model Performance 
![Model Performance](https://user-images.githubusercontent.com/61132761/219288645-06a0835b-b980-4a4e-8c8d-f8c66a2aa3aa.jpg)

# Misclassified Images 
![Misclassified Images](https://user-images.githubusercontent.com/61132761/219288916-510e35c8-9339-4d85-b93d-28106288553b.jpg)

# GradCAM Output for the Misclassified Images
![Gradcam](https://user-images.githubusercontent.com/61132761/219289244-f958a44c-6bba-48dd-9abc-541142845ff6.jpg)

# External Reference Used
https://github.com/jacobgil/pytorch-grad-cam
