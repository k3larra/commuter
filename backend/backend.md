### ML-Backend connected to Skånependlaren commuter app.
The general outline of the backend  that connects tha app and the machine learning is oulined below. Our overaching goal has been to save training data and train one ML model separate for each user. Our context gives us some metrics that we need to target. One is of course accuracy, another is response time and training time. Aspects of the accuracy is a more complex issue and will be discussed below, response time for a prediction given the application has to be counted in a few seconds. This targets the situation when you start the app and as soon as possible want to have departure time for next transport.


![Backend](images/backend_skanependlaren.png)
*Figure 1: Backend that saves labelled data from the app and delivers predictions to the app. When new labelled data is entered by the user (this could be done explicitly or when the user selects a new route) the labelled data is saved and can be used for training. The coordination for this is done via the real-time database and cloud functions. Retraining is currently done one hour after the last use of the app. Predictions are initiated when the user/app uploads features (weekday, time, location, activity) to the real-time database and the Node.JS performs the predictions and returns the result via the real-time database.*

### Verification of backend functionality
Initial we wanted to make a technical verification that uses the backend and delivers predictions in the app. We reached our main metric for the backend and can deliver predictions in most cases in a few seconds. These test were mostly to verify the functionality. An animation that visualize a prediction can be seen on this [site](https://skanependlaren.firebaseapp.com/).

#### Verification of ML functionality
The focus is not only on optimising the ML algorithm used, of course we want to have accurate predictions, but there are other parameters that has to be taken into account as for example.
* Ease of use
* Generabizability of the algorithm so it can handle a varying amount of data, concept drift and different of use patterns.
* Online inference
* Scalability so each user can have her/his own model.
In our experimentation we did initially work with [tensorflow](https://www.tensorflow.org) and tried out different ML algorithms by using [estimators](https://www.tensorflow.org/guide/estimators). Given our data and our competence in the area these solutions took a lot of time especially in handling with normalisation of parameters tuning and saving the models correctly so inference could be made online. In parallel we evaluated [Fastai](https://www.fast.ai/) framework that builds on [PyTorch](https://pytorch.org/) and found that the abstraction level that framework represents was more in line with our needs. The evaluations below uses Pytorch 1.0 and Fastai 1.0.

Our initial tests with fastai [tabular learner](https://docs.fast.ai/tabular.html) and a neural network with [two hidden layers](ml/baseline.ipynb) gave us predictions that met our expectations regarding accuracy. To evaluate this in a more structured way we created some idealised data using our [personas](#Personas) and senarios. The data was created using our app and the result of the evaluation can be seen in Figure 3 and more details and discussion exists in the persona descriptions.
