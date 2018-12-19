# Commuting and Machine Teaching
The focus in this project is initially on exploring if and how a Machine Teaching<sup>1</sup> approach can mitigate consequenses of cold start in a commuter app. The commuter app [Skånependlaren(https://play.google.com/store/apps/details?id=se.k3larra.alvebuss&hl=sv) focuses on presenting departure times in the near future as efficient as possible. The target group is commuters and consequently there is no interface in the app for planning, bying tickets or other more high level functionality. The situation targeted is from a few hours before departure until departure. The [app](https://play.google.com/store/apps/details?id=se.k3larra.alvebuss&hl=sv) in the version that exists publicly prior to this project delivers departure times including delays, first change in transportaion mode and total travel time for the journey.

### Journey patterns
A commuters journey pattern is an interesting machine lerarning problem for our research since it uses a limited amount of data, the stations in Skåne region, and the travel pattern over time are relativelly unique for the individual user. Since the journey consistiong of origin destination and not the departure station is in focus a commter app it would be difficoult to predict a users next journey except as a guessing based on statistical travel data that predict most common journey in a given situation.

### Individual approach
Since our  primary research interest is around how Machine Learning(ML) can simplify for individuals and thus the focus is on the individual experience and not som much the comparison with other users. The context of commuting fits well into those research interests. Another factor that is important to us is that, even if we handle personal data, travel patterns are mostly sensitive if they can be connected to a person. In this work we [avoid saving data](https://skanependlaren.firebaseapp.com) that can be used to identify individuals. We do also give the users an option to delete all collected data and trained models.

### Methodology
In this project we use a Research through Design<sup>2</sup> methodology and this site with its history represents our documentation of the explorative process.

## ML-Backend connected to Skånependlaren commuter app.
The general outline of the backend is illustrated below. Our overaching goal has been to save training data and train one ML model separate for each user. Our context gives us some metrics that we need to taget. One is of course accuracy and another is response time. Aspect of the accuracy is a more complex issue and will be discussed below, resonse time for a prediction given the application has to be counted in a few seconds. This targets the situation when you start the app and as soon as possible want to have departure time for next transort.

### System architecture

![Backend](https://github.com/k3larra/commuter/blob/master/images/backend_skanependlaren.png)

*Backend that saves labelled data from the app and delivers predictions to the app. When new labelled data is entered by the user (this could be done explicitly or when the user selects a new route) the labelled data is saved and can be used for training. The coordination for this is done via the real-time database and cloud functions. Retraining is currently done one hour after the last use of the app. Predictions are initiated when the user/app uploads features (time,location,accuracy) to the real-time database and the Node.JS performs the predictions and returns the result via the real-time database.*

### Initial research approach
We have implented the backend described in System Architecture and our focus is now on the uses first encounter with the app. In this situation the app has no knowledge of the users commute patterns and can thus not make any predictions. The commute patterns can be learned over time and it will probably take a few weeks until enough training data has been collected to make accurate journey predictions. In this work we want to explore a Machine Teaching approach that involves an initial Machine Teaching session where known travel patterns are added. In this work the focus is not so much on the ML algorithm used instead our focus is exploring the user experience in an initial phase.
[Link](Sources of errors that exists in the real world application)

[Work or not?](###system-architecture)


### Data from fictional personas (#data-from-fictional-personas)
For initial evaluation regarding the journey predictions we have created three fictive personas and some scenarios for these personas to help us recreate and simulate situations. The personas and scenarios are presented below.

For each user labelled data has been created that matches the users travel patterns. This data especially differs from real world data in the sense that it only contains valid searches and no erroneous data.

#### Sources of errors that exists in the real world application
Typical errors that exists in real data are due to the constuction of the [app](https://skanependlaren.firebaseapp.com/) and usage. Example of invalid data coming from the construction is the two dropdowns at the top and tha fact that journey searches are done directely when the user changes one of them, there is no way to tell if you plan to change both origin and destination, and thus create two searches or if changing one of them is sufficient. At the moment we do not have an algoritm that filters serches and tries to find the one that is relevant. There are of course also situations where a user explores possible routes whitout the intention of conductiong them even in the near future.

For all scenarios, test data has been created to evaluate prediction accuracy for each situation. For each user labelled data is aggregated after one week of use, one month of use and one year of use.

### [Maria](Maria.md)
Maria labelled training/development data.
Maria test data
tnK534JMwwfhvUEycn69HPbhqkt2.csv

### [Björn](Bjorn.md)
Björn labelled training/development data.
Björn test data
hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2.csv

### [Andrea](Andrea.md)
Andrea labelled training/development data.
Andrea test data
ehaBtfOPDNZjzy1MEvjQmGo4Zv12.csv

## Skånependlaren app
The app that has been used for this work can be downloaded from google play [Skånependlaren](https://skanependlaren.firebaseapp.com/)

<hr>
Images on the pages are owned by the author or if stated otherwise collected from [pixabay](https://pixabay.com) and licenced under [CC0 Creative Commons]( https://creativecommons.org/publicdomain/zero/1.0/deed.en)
_References_

[1] P. Y. Simard et al., “Machine Teaching: A New Paradigm for Building Machine Learning Systems,” 2017.

[2] P. Stappers and E. Giaccardi, “Research through Design,” Encycl. Human-Computer Interact. 2nd ed.; Idea Gr. Ref. Hershey, PA, USA, pp. 1–94, 2017.
