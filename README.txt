To set up the required packages, please install the following:

- pip install opencv-contrib-python
- pip install ultralytics

I leverage a Google Colab environment for training the Convolutional Neural Network (CNN), a decision driven by its capability to utilize 
a dedicated cloud GPU. This significantly reduces the training time, enabling me to experiment with 
various options, such as increasing the number of epochs.

For insights into the CNN training process and specifications, refer to the document at the following link:

https://colab.research.google.com/drive/1_JGDRfOkz-sghz_EEKE6XR285P9jqImb?usp=sharing

The "Img detector" program employs the trained model (best.pt) to identify papayas in images, while 
the "Camera detector" program performs real-time papaya recognition using the same model (best.pt).

The "pr" program serves the purpose of organizing and specifying the dataset images.

"I.D.G." (Image Data Generator) is the program I utilized to generate a larger volume of images 
for the dataset. It applies various transformations 
to a base image, creating diverse images suitable for training.

For image segmentation and data extraction in JSON format, I utilize the Labelme tool.

yolov8x-seg 
