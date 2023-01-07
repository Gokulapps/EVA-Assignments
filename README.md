# EVA-Assignments
This is the First Assigment in EVA Course where we need to train the Model with the Custom Dataset using Pytorch. 

Data Generation Strategy - The Data Generation Strategy for both the Models are Same. I created CustomDataset class for Generating the Dataset. It accepts fashion MNIST Dataset along with its size as a Input and Generates Random Number from 0 - 9 equal to the Size of Input Dataset through torch.randint() Function and converts them into 10 digits using one hot Encoding. Then Generates Labels for Random Number by adding Labels of Fashion MNIST Dataset to the Random Number. Finally merges the Fashion MNIST Data and Random Number Data along with its Labels in a List of tuple.

Method for Combining Both the Inputs - For the First Model I Combined the Random Number Data at Fully Connected Layer. As Fully Connected Layer takes Flattened Input, I Concatenated the Convoluted Ouput of an Image with Random Number through torch.cat() Function. For the Second Model  I replaced the Last 10 Pixels of an Image with the 10 randomly generated number before passing it to the Neural Network. 

Loss Function - I have used Cross Entropy for both the Models that i trained. I prefered this Loss Function over the other Function for its Simplicity. I was able to easily Evaluate the accuracy of the Model with this Function. As the Values is between 0 - 1, it was easier to Evaluate my Model.

