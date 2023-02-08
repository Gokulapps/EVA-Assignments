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

![image](https://user-images.githubusercontent.com/61132761/217616580-7577723b-1a7c-4416-9923-cdca7a9231e8.png)


                                                 The Plot for Network's Accuracy and Loss

![image](https://user-images.githubusercontent.com/61132761/217616902-c56402fb-3d1c-4623-93e6-8d4d43ef12fe.png)


                            Ten Misclassified Images by the Network is shown below to Understand the shortcomings of the Model

![image](https://user-images.githubusercontent.com/61132761/217617038-91b778cd-12cc-49d3-a24b-f89b5bd2732b.png)

