# ML-Backend supporting Skånependlaren commuter app.
This information is a complement to the [general information](https://skanependlaren.firebaseapp.com/) around the Skånependlaren. The information here concerns the ML-backend and how the predictions are made. In this documentation we present the code for predictions, labelled data and test data. The general outline of the backend is illustrated below.

## System description

![Backend](https://github.com/k3larra/commuter/blob/master/images/backend_skanependlaren.png "Little image")

*Backend that saves labeled data from tha app and delivers predictions to the app. When new labeled data is entered by the user (this could be done explicitly or when the user selects a new route) the labeleld data is saved and can be used for training. The corination for this is done via the realtime database and cloud functions. Retraining is currently done one hour after the last use of the app. Predictions are initiated when the user/app uploads features (time,location,accuracy) to the realtime database and the Node.JS performs the predictions and returns the result via the realtime database.*


## Fictional personas
To evaluate the predictions we have created three fictive personas. We have also creted some scenarions for these personas to help us recreate and simulate situations. The personas and scenarious are presented below. For each user labelled data has been created that matches the users travel pattern for one year. For all scenarions test data has been created to evaluate prediction accuracy for each situation.
For each user labeled data is agregated after one week of use, one month of use and one year of use.

### [Maria](Maria.md)
Maria labeled training/development data.
Maria test data
tnK534JMwwfhvUEycn69HPbhqkt2.csv

### [Björn](Bjorn.md)
Björn labeled training/development data.
Björn test data
hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2.csv

### [Andrea](Andrea.md)
Andrea labeled training/development data.
Andrea test data
ehaBtfOPDNZjzy1MEvjQmGo4Zv12.csv

## Skånependlaren app
The app that has been used for this work can be downloaded from google play [Skånependlaren](https://skanependlaren.firebaseapp.com/)

Images on the pages are owned by the author or if stated collected from [pixabay](https://pixabay.com) and licenced under [CC0 Creative Commons]( https://creativecommons.org/publicdomain/zero/1.0/deed.en)
