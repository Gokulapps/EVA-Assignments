# EVA-Assignments
This is the First Assignment in EVA Course where we need to train the Model with the Custom Dataset using Pytorch. I have mentioned some of the Strategies that i used for training the Model Below,

Data Generation Strategy - The Data Generation Strategy for both the Models are Same. I created CustomDataset class for Generating the Dataset. It accepts fashion MNIST Dataset along with its size as a Input and Generates Random Number from 0 - 9 equal to the Size of Input Dataset through torch.randint() Function and converts them into 10 digits using one hot Encoding. Then, it Generates Labels for Random Number by adding Labels of Fashion MNIST Dataset to the Random Number. Finally merges the Fashion MNIST Data and Random Number Data along with its Labels in a List of tuple.

Method for Combining Both the Inputs - For the First Model I Combined the Random Number Data at Fully Connected Layer. As Fully Connected Layer takes Flattened Input, I Concatenated the Convoluted Ouput of an Image with Random Number through torch.cat() Function. For the Second Model  I replaced the Last 10 Pixels of an Image with the 10 randomly generated number before passing it to the Neural Network. 

Loss Function - I have used Cross Entropy for both the Models that i trained. I prefered this Loss Function over the other Function for its Simplicity. I was able to easily Evaluate the accuracy of the Model with this Function. As the Values is between 0 - 1, it was easier to Evaluate my Model.

Method of Evaluation - I created a Function to Evaluate the Model. I basically Used Test Dataset to Evaluate my Model. The Function takes Model and the Test Dataset on which the Model needs to be tested as input and returns accuracy. For the two Models I used, I got better results for the First Model which combines both the Input at Fully Connected Layer. Still the Accuracy is just 2.61% which is low in General. 

