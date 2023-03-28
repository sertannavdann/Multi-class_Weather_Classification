# Weather Detection

This repository contains the implementation of a Weather Detection model using deep learning techniques with PyTorch. 

- We have freeze the top layers of MobileNetV2 and use only the lowest pretrained modules to start our training!
- It reacted much better than expected.

The model is designed to classify Weather conditions. There are couple helper functions in the code for 

1. Foldering
2. Augmenting & Balancing
3. Merging & Splitting

Those are configuration of my previous work for this specific task.

### Categories for this model:
['cloudy', 'rain', 'shine', 'sunrise']

### Accuracy score
- We had a almost %100 accuracy. Our model is designed according to academic researches.
- Data augmentations are highlighting variety of different features for CNN model.
- Our model is behaving really good in the wild deployment.

![Alt text](/accuracy_graph.png "Score")


    

