### ML-Backend connected to Skånependlaren commuter app.
The general outline of the backend  that connects tha app and the machine learning is oulined below. Our overaching goal has been to save training data and train one ML model separate for each user. Our context gives us some metrics that we need to target. One is of course accuracy, another is response time and training time. Aspects of the accuracy is a more complex issue and will be discussed below, response time for a prediction given the application has to be counted in a few seconds. This targets the situation when you start the app and as soon as possible want to have departure time for next transport.


![Backend](../images/backend_skanependlaren.png)
*Figure 1: Backend that saves labelled data from the app and delivers predictions to the app. When new labelled data is entered by the user (this could be done explicitly or when the user selects a new route) the labelled data is saved and can be used for training. The coordination for this is done via the real-time database and cloud functions. Retraining is currently done one hour after the last use of the app. Predictions are initiated when the user/app uploads features (weekday, time, location, activity) to the real-time database and the Node.JS performs the predictions and returns the result via the real-time database.*

### Verification of backend functionality
Initial we wanted to make a technical verification that uses the backend and delivers predictions in the app. We reached our main metric for the backend and can deliver predictions in most cases in a few seconds. These test were mostly to verify the functionality. An animation that visualize a prediction can be seen on this [site](https://skanependlaren.firebaseapp.com/).
