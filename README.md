# Weather Detection



This repository contains the implementation of a Weather Detection model using deep learning techniques with PyTorch. 

- We have freeze the top layers of MobileNetV2 and use only the lowest pretrained modules to start our training!
- It reacted much better than expected.

The model is designed to classify Weather conditions. There are couple helper functions in the code for 

1. Foldering
2. Augmenting & Balancing
3. Merging & Splitting

Those are configuration of my previous work for this specific task.

- You can reach the [Dataset](https://data.mendeley.com/datasets/4drtyfjtfy/1). 

### Categories for this model:
['cloudy', 'rain', 'shine', 'sunrise']

### Accuracy score
- We had above %92 accuracy in all of our tests from google images.

- The model architecture is detailly designed in accordance with François Chollet's book.

- Data augmentations are highlighting variety of different features for CNN model.
- Our model is behaving really good in the wild deployment.

![Accuracy](/accuracy_graph.png "Score")
![LossGraph](/loss_graph.png "Loss")

    

