This Folder consists of Session 2.5 Pytorch Assignment where we need to train the Model with the Custom Dataset using Pytorch. The Network is Designed in such a way that it accepts two Inputs and produces two Outputs. One of the Input to the Network is Image from Fashion MNIST Dataset and the other Input is Random Number from 0 - 9 represented in 10 digits. I have created two Neural Network as part of this Assignment and both the Network are Trained for 10 Epochs. Below, I have mentioned some of the Strategies that i used for training the Model.

Data Generation Strategy - The Data Generation Strategy for both the Models are Same. I created CustomDataset class for Generating the Dataset. It accepts fashion MNIST Dataset along with its size as a Input and Generates Random Number from 0 - 9 equal to the Size of Input Dataset through torch.randint() Function and converts them into 10 digits using one hot Encoding. Then, it Generates Labels for Random Number by adding Labels of Fashion MNIST Dataset to the Random Number. Finally merges the Fashion MNIST Data and Random Number Data along with its Labels in a List of tuple.

Method for Combining Both the Inputs - For the First Model I Combined the Random Number Data at Fully Connected Layer. As Fully Connected Layer takes Flattened Input, I Concatenated the Convoluted Ouput of an Image with Random Number through torch.cat() Function. For the Second Model I replaced the Last 10 Pixels of an Image with the 10 randomly generated number before passing it to the Neural Network.

Loss Function - I have used Cross Entropy for both the Models that i trained. I prefered this Loss Function over the other Function for its Simplicity. I was able to easily Evaluate the accuracy of the Model with this Function. As the Values is between 0 - 1, it was easier to Evaluate my Model.

Method of Evaluation - I created a Function to Evaluate the Model which will Use Test Dataset to Evaluate the Model. The Function takes Model and the Test Dataset on which the Model needs to be tested as input and returns accuracy based on Nuber of Correct Predictions in Test Dataset. For the two Models I used, I got Accuracy of 0.975% for the First Model and 7.34% for the Second Model. From this results we can Infer that Model in which we replaced the Last Ten Digits of the Input Image with Random Number fared comparatively better than the other Model which Combined them at Fully Connected Layer. Still the Accuracy for both the Models are too Low.   

**Please Find the Training Logs for Network 1 below **

Epoch 1 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4858.6908826828
Total Number of Correct Predictions for both the Outputs : 779
Epoch 2 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4807.182219028473
Total Number of Correct Predictions for both the Outputs : 1134
Epoch 3 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4810.719478130341
Total Number of Correct Predictions for both the Outputs : 1125
Epoch 4 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4807.289442062378
Total Number of Correct Predictions for both the Outputs : 1050
Epoch 5 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4832.140815734863
Total Number of Correct Predictions for both the Outputs : 818
Epoch 6 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4908.256883621216
Total Number of Correct Predictions for both the Outputs : 585
Epoch 7 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4908.256883621216
Total Number of Correct Predictions for both the Outputs : 585
Epoch 8 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4908.210008621216
Total Number of Correct Predictions for both the Outputs : 585
Epoch 9 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4908.147508621216
Total Number of Correct Predictions for both the Outputs : 585
Epoch 10 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4908.163133621216
Total Number of Correct Predictions for both the Outputs : 585
Model Training Completed!!!!

**Please Find the Training Logs for Network 2 below **

Epoch 1 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4891.879001617432
Total Number of Correct Predictions for both the Outputs : 586
Epoch 2 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4837.478260040283
Total Number of Correct Predictions for both the Outputs : 1009
Epoch 3 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4591.615690231323
Total Number of Correct Predictions for both the Outputs : 2653
Epoch 4 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4487.286405086517
Total Number of Correct Predictions for both the Outputs : 3477
Epoch 5 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4458.471816539764
Total Number of Correct Predictions for both the Outputs : 3647
Epoch 6 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4447.959843158722
Total Number of Correct Predictions for both the Outputs : 3829
Epoch 7 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4439.609226703644
Total Number of Correct Predictions for both the Outputs : 3822
Epoch 8 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4435.454688549042
Total Number of Correct Predictions for both the Outputs : 3879
Epoch 9 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4402.789065361023
Total Number of Correct Predictions for both the Outputs : 4169
Epoch 10 Result :-
Total Images Processed in this Epoch : 60000
Loss for this Current Epoch : 4369.406797409058
Total Number of Correct Predictions for both the Outputs : 4399
Model Training Completed!!!!
