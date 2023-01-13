Part 1

This Folder has Excel File along with some Images as a Part 1 Assignment where the Gradients and BackPropagation values for a Simple FC Network (shown in Excel File) is Calculated and tested with different Values of Learning Rate. In the Excel File, all the Major Steps required to calculate the BackPropagation Values is mentioned along with Network Diagram. Attaching Below Some Images for the Loss Graph Calculated with different Values of Learning Rate along with the Screenshot depicting the Entire BackPropagation Process.

                                                   Entire BackPropagation Values calculated for the Network
![image](https://user-images.githubusercontent.com/61132761/211786005-d70d28e3-40d4-468a-8e81-35174baf376e.png)

Loss Graph with Learning Rate = 0.1

![image](https://user-images.githubusercontent.com/61132761/211786408-f3a531df-54a9-4ed1-8a5d-7e5149b94143.png)

Loss Graph with Learning Rate = 0.2

![image](https://user-images.githubusercontent.com/61132761/211786686-b0b6907c-3fa9-455b-bc9f-79aad0115381.png)

Loss Graph with Learning Rate = 0.5

![image](https://user-images.githubusercontent.com/61132761/211786867-675ee3b5-c6cf-42b8-890f-4fa646fb5674.png)

Loss Graph with Learning Rate = 0.8 

![image](https://user-images.githubusercontent.com/61132761/211787099-94627cf8-d6b2-42e7-a12d-8e2db6ef30a7.png)

Loss Graph with Learning Rate = 1.0

![image](https://user-images.githubusercontent.com/61132761/211787379-321e80e2-f4d7-4e08-a350-e75f2c648bff.png)

Loss Graph with Learning Rate = 2.0

![image](https://user-images.githubusercontent.com/61132761/211787528-14eb7408-6f81-4c64-a6bf-1bab6aaf550e.png)

Part 2 

I have designed a Neural Network with 17,410 Parameters using Pytorch which can reach a Maximum Validation Accuracy of 99.41% on MNIST Test Dataset. The Network was Trained on MNIST Train Dataset for less than 20 Epochs. The Architecture of the Network is shown below 

----------------------------------------------------------------
        Layer (type)               Output Shape           Param 
================================================================
            Conv2d-1            [-1, 8, 24, 24]             208
       BatchNorm2d-2            [-1, 8, 24, 24]              16
            Conv2d-3           [-1, 16, 20, 20]           3,216
       BatchNorm2d-4           [-1, 16, 20, 20]              32
            Conv2d-5             [-1, 32, 6, 6]          12,832
       BatchNorm2d-6             [-1, 32, 6, 6]              64
         Dropout2d-7             [-1, 32, 6, 6]               0
            Conv2d-8             [-1, 24, 6, 6]             792
         AvgPool2d-9             [-1, 24, 1, 1]               0
           Linear-10                   [-1, 10]             250
================================================================
Total params: 17,410
Trainable params: 17,410
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.20
Params size (MB): 0.07
Estimated Total Size (MB): 0.27
----------------------------------------------------------------

Training Logs for the Network is shown below :- 

loss=0.0471455343067646 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 33.04it/s]

Test set: Average loss: 0.0923, Accuracy: 9758/10000 (98%)

loss=0.057915911078453064 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.39it/s]

Test set: Average loss: 0.0625, Accuracy: 9816/10000 (98%)

loss=0.023455316200852394 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.56it/s]

Test set: Average loss: 0.0429, Accuracy: 9875/10000 (99%)

loss=0.026261910796165466 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.83it/s]

Test set: Average loss: 0.0379, Accuracy: 9886/10000 (99%)

loss=0.05324679613113403 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 33.12it/s]

Test set: Average loss: 0.0382, Accuracy: 9889/10000 (99%)

loss=0.006078144069761038 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.23it/s]

Test set: Average loss: 0.0294, Accuracy: 9913/10000 (99%)

loss=0.01567075215280056 batch_id=468: 100%|██████████| 469/469 [00:15<00:00, 30.48it/s]

Test set: Average loss: 0.0309, Accuracy: 9905/10000 (99%)

loss=0.021045304834842682 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.71it/s]

Test set: Average loss: 0.0340, Accuracy: 9903/10000 (99%)

loss=0.03431989625096321 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 33.25it/s]

Test set: Average loss: 0.0243, Accuracy: 9926/10000 (99%)

loss=0.04197216406464577 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 33.18it/s]

Test set: Average loss: 0.0287, Accuracy: 9908/10000 (99%)

loss=0.03104185312986374 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 33.40it/s]

Test set: Average loss: 0.0253, Accuracy: 9916/10000 (99%)

loss=0.013290449976921082 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.61it/s]

Test set: Average loss: 0.0211, Accuracy: 9941/10000 (99%)

loss=0.035811688750982285 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.92it/s]

Test set: Average loss: 0.0246, Accuracy: 9926/10000 (99%)

loss=0.08837571740150452 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.99it/s]

Test set: Average loss: 0.0216, Accuracy: 9933/10000 (99%)

loss=0.09227914363145828 batch_id=468: 100%|██████████| 469/469 [00:14<00:00, 32.77it/s]

Test set: Average loss: 0.0253, Accuracy: 9927/10000 (99%)
