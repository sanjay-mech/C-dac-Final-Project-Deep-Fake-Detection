# DeepFake Detection Using MTCNN and MesoNet3

## Project Overview

The goal of this project is to develop a robust and efficient system for detecting deepfake videos using a combination of computer vision techniques, specifically MTCNN (Multi-task Cascaded Convolutional Networks), and a deep learning model called MesoNet3. This system will be designed to accurately identify manipulated facial images and videos created through deepfake technology, thereby helping to combat the spread of misleading or fraudulent content.

## Project Objectives

### 1. DeepFake Detection

Implement MTCNN to detect and localize faces within video frames or images. This step is crucial for isolating and analyzing facial regions within the content.

### 2. Feature Extraction

Utilize MesoNet3, a deep learning model specifically designed for deepfake detection, to extract features from the facial regions detected by MTCNN. MesoNet3 is known for its effectiveness in identifying subtle artifacts and irregularities in deepfake content.

### 3. Model Training

Train the MesoNet3 model on a diverse dataset of both real and deepfake videos and images. The dataset should encompass various manipulation techniques and scenarios to ensure the model's robustness.

### 4. Evaluation

Evaluate the model's performance on a separate test dataset, measuring its accuracy, precision, recall, and F1-score in detecting deepfake content. Conduct additional analysis to assess its robustness against various deepfake generation methods.

### 5. Integration

Integrate the MTCNN and MesoNet3 models into a unified deepfake detection pipeline. This system should accept video streams or image files as input and provide output indicating whether deepfake content is detected and where it is located within the media.



### 6. Deployment

Deploy the deepfake detection system on a suitable platform, such as a web service, mobile application, or on-premises server, depending on the intended use case. We used Streamlit for project Deployment.

## Introduction

This project aims to detect video deepfakes using deep learning techniques like MTCNN and MesoNet3. We have achieved deepfake detection by using transfer learning, where the pretrained MesoNet3 model is employed.

## Dataset

We have used the FaceForensics Deepfake dataset. The dataset can be accessed from the following link: [Kaggle FaceForensics Dataset](https://www.kaggle.com/datasets/sorokin/faceforensics)
