# ![Fruit Classifier Logo](https://github.com/Ghost-141/Fruit-Vegetable-Classifier/blob/fbbcbb6d6303e56bd00a6647bcc4893dd18aa01f/cover%20image.jpg) Fruit-Vegetable-Classifier
A Deep Learning model designed to classify images of fruits and vegetables into their respective categories. This repository contains a pre-trained model, a Jupyter notebook demonstrating the training process, and a Gradio-powered web interface for testing the classifier. You can use the docker file[`Dockerfile`](Dockerfile) to run and test the model on your local machine.

## Table of Contents
- [Introduction](#introduction)
- [Usage](#usage)
- [Features](#features)
- [Installation](#installation)
- [Model Info](#model-training)
- [Future Work](#future-work)

## Introduction
This projects utilizes the power of CNN (Convolutional Neural Network) to Classify between fruit and vegetable across 36 different classes. This project utilized the power of custom cnn model to classify between fruit and vegetable. 
[Dataset](https://www.kaggle.com/kritikseth/fruit-and-vegetable-image-recognition)

## Usage
- Download the folder and enjoy
- Ensure that the pre-trained [`custom_cnn_model.h5`](custom_cnn_model.h5) file is in the project directory
- Run the [`classify.py`](classify.py) file to launch the web-interface and enjoy the app
   
## Features
- Custom pre-trained model for quick use on classification task
- Jupyter notebook to demonstrate the whole process of model training and testing
- Gradio web interface for easy testing and interaction   

## Installation
To use the notebook follow the steps to install dependencies given below:
- For pip installation use command `pip install -r requirements.txt`
- For conda installation use command `conda install --file requirements.txt`
- Make sure to run the commands in administrator mode to avoid any issue.

To test the app using docker file to use the following instrctions:

- download the [docker desktop](https://www.docker.com/products/docker-desktop/) app based on your OS

- Use the following command to build and run the docker image:
```bash
docker build -t app_name .
docker run -p port_name:7860 classifier
```
- open any browser and go to http://localhost:port_name to perform inference

## Model Info
- Achieved an accuracy of 93% on test dataset
- Model was trained for 40 epochs
- Used tensorflow framework to develop the model
- Implemented an early stopping callback to prevent overfitting during model training

## Future Work
- Optimize model for mobile devices
- Optimize the docker image for better performance
- Use FastAPI/Flask to serve the model


