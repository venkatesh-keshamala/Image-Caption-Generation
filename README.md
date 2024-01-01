An Efficient Deep Learning based Hybrid Model for
Image Caption Generation


# Description

This project aims to develop a hybrid image captioning approach using an encoder-decoder model with xception. xception is employed as pre-trained feature extraction models, leveraging knowledge from millions of images. The results from these models are concatenated into a single file. Subsequently, Long Short-Term Memory (LSTM) model is employed for generating textual descriptions of the images.

#Key Components


These pre-trained models serve as feature extraction engines, leveraging knowledge gained from a vast dataset of images.

Encoder-Decoder Architecture:

The heart of the system lies in its encoder-decoder architecture, where the extracted features are processed through LSTM to generate descriptive textual captions.

#Workflow

Feature Extraction:

Xception model is used to extract intricate features from images, capturing both spatial and semantic information.

Concatenation:

The features extracted from the three models are concatenated into a unified representation, forming a comprehensive feature set.

Textual Description Generation:

LSTM process is the concatenated features to generate natural language descriptions, encapsulating the essence of the visual content.

Getting Started:

```bash
1.Clone the repository:

https://github.com/venkatesh-keshamala/Image-Caption-Generation.git
 
2.Install dependencies:

pip install -r requirements.txt

```
    
## How To Run
Command to run this project:

python manage.py runserver
## Authors

- [@venkatesh-keshamala](https://www.github.com/venkatesh-keshamala)




RESULTS:

![dog](https://github.com/venkatesh-keshamala/Image-Caption-Generation/assets/116023226/fe623b6b-e78b-47fc-9ed1-2c5836ba1fc3)
