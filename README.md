# Commuting and Machine Learning and Machine Teaching
*In this project we explore in what way Machine Learning (ML) can be used to personalize and improve performance in a commuter app using the contextual parameters (time, day, location and activity). We will focus on an interactive approach to Machine Learning (iML) in a series of experiments. We have selected commuting and [commute patterns](Commute_patterns) since it is an area that has some characteristics that suits iML well especially the fact that it is hard to deduce one users commute patterns from other users. From a ML perspective training our ML-artifact is an online learning situation that includes cold start, outlier data, data cleaning, concept drift and aging data. In the project we will also study if and how a iML approach changes the users feeling of ownership both with respect to the training and to the collected data.*

The existing non ML commuter app [Skånependlaren](https://play.google.com/store/apps/details?id=se.k3larra.alvebuss&hl=sv) focuses on presenting departure times in the near future as efficient as possible. The target group for the app is commuters and consequently there is no interface in the app for planning, buying tickets or other more high level functions. The situation targeted is getting departure times from a few hours before departure until departure. The [app](https://play.google.com/store/apps/details?id=se.k3larra.alvebuss&hl=sv) that has existed prior to this project delivers departure times including delays, first change in transportaion mode and total travel time for the journey.

### Commute patterns
A commuters journey pattern is an interesting machine learning problem for our research since it uses a limited amount of data, the stations in Skåne region, and the travel pattern over time are relativelly unique for the individual user. Since we focus on journeys that consists of origin destination and not on predictiong only the departure station it would be difficult to predict a users next journey except as a guessing based on statistical travel data that predict most common journeys for all in a given situation.

### Individual approach
Since one of aour research interest is around how Machine Learning(ML) can be personalized the focus is on the individual experience and not so much the comparison with other users. The context of commuting fits well into those research interests. Another factor that is important to us is that, even if we handle personal data, travel patterns are high sensitive and can mostly be missued if they can be connected to a person. In this work we [avoid saving data](https://skanependlaren.firebaseapp.com) that can be used to identify individuals. We do also give the users an option to delete all collected data and trained models.

### Methodology
In this project we use a Research through Design<sup>2</sup> methodology and this site with its history represents our documentation of the explorative process.

### Project process.
The sections referensed below represents the initial steps in our explorative process.
* [ML backend](#ML_backend)
* [Verification of backend_functionality](#Verification_of_backend_functionality)
* [Initial MT approach](Initial_MT_research_approach)
  * [Verification of ML functionality](Verification_of_ML_functionality)
  * [Evaluation of simple MT interface](Evaluation_of_MT_interface)
* [Use study MT approach handling cold start situation](User_study_MT_approach_handling_cold_start_situation)
* [Use study iterative ML used to update the ML model]()
* [Use study interactive ML in kombination with iterative ML]()
* [Use study MT, interactive ML and iterative ML]()

## Process documentation
Initially in the project we will, as the plan above indicates, focus on the commuters first encounter with the app and the task of training an ML-model so the app can make predictions for her/his recurrent journeys. We will use a Machine Teaching<sup>1</sup> (MT) approach to mitigate the consequences of this cold start problem. After this we will verify our approach and test it in a use situation. After this initial stage we will explore iML during app use in a more longitudial survey.

### ML-Backend connected to Skånependlaren commuter app.
The general outline of the backend is illustrated below. Our overaching goal has been to save training data and train one ML model separate for each user. Our context gives us some metrics that we need to target. One is of course accuracy and another is response time. Aspect of the accuracy is a more complex issue and will be discussed below, response time for a prediction given the application has to be counted in a few seconds. This targets the situation when you start the app and as soon as possible want to have departure time for next transport.


![Backend](images/backend_skanependlaren.png)
*Figure 1: Backend that saves labelled data from the app and delivers predictions to the app. When new labelled data is entered by the user (this could be done explicitly or when the user selects a new route) the labelled data is saved and can be used for training. The coordination for this is done via the real-time database and cloud functions. Retraining is currently done one hour after the last use of the app. Predictions are initiated when the user/app uploads features (weekday, time, location, activity) to the real-time database and the Node.JS performs the predictions and returns the result via the real-time database.*

### Verification of backend functionality
Initial we wanted to make a technical verification that uses the backend and delivers predictions in the app. We reached our main metric for the backend and can deliver predictions in most cases in a few seconds. These test were mostly to verify the functionality. An animation that visualize a prediction can be seen on this [site](https://skanependlaren.firebaseapp.com/).

### Initial MT research approach
Our focus in this part of the work is on the users first encounter with the app. In this situation the app has no knowledge of the users commute patterns and can thus not make any predictions. The commute patterns could be learned over time but it will probably take a few weeks until enough training data has been collected to make accurate journey predictions. In our initial approach we are interested of transferring the commuters knowledge of his/her commute patterns to the ML artifact. Initially we want to explore and evaluate a MT approach that starts with an initial Machine Teaching session. In this session the user adds known travel patterns and that can be used to train the model so predictions can be made from first use.

![Backend](images/small_detail_search.png)
![Backend](images/small_prediction.png)
![Backend](images/training.png)

**Figure 3:** *In the figure on the left the standard app is shown and details for one departure is expanded. In the second figure the app has received a contextbased prediction and departure times has been collected from the transport provider. In the figure on the right labelled training data can be added.*


#### Verification of ML functionality
The focus not only on optimising the ML algorithm used, of course we want to have accurate predictions, but there are many other parameters that has to be taken into account as for example.
* Ease of use
* generabizability of the algorithm so it can handle a varying amount of data, concept drift and different of use patterns.
* Online inference, scalability so each user can have her/his own model.
In our experimentation we did initially work with [tensorflow](https://www.tensorflow.org) and tried out different ML algorithms by using [estimators](https://www.tensorflow.org/guide/estimators). Given our data and our competence in the area these solutions took a lot of time especially in handling with normalisation of parameters tuning and saving the models correctly so inference could be made online. In parallel we evaluated [Fastai](https://www.fast.ai/) framework that builds on [PyTorch](https://pytorch.org/) and found that the abstraction level that framework represents was more in line with our needs. The evaluations below uses Pytorch 1.0 and Fastai 1.0.

Our initial tests with fastai [tabular learner](https://docs.fast.ai/tabular.html) and a neural network with [two hidden layers](ml/baseline.ipynb) gave us predictions that met our expectations regarding accuracy. To evaluate this in a more structured way we created some idealised data using [personas](#Personas) and senarios. The data was created using our app and the result of the evaluation can be seen in Figure 3 and more details and discussion exists in the persona descriptions.

![](images/AndreaTraining.png).

**Figure 3:** *This figure shows training accuracy during the two first weeks of use, starting from a Saturday. All trained models accuracy are evaluated using the same test set. The blue line represents a Cold Start situation when no data exists to train from. The red line represents a more traditional ML setting were relevant training data is aviable before the model is deployed and used, in this case the data described above from one year of usage is used for the training. The green and orange lines represents a situaion were a teaching set is added in advance.*

#### Evaluation of MT interface
In progress
### User study MT approach handeling cold start situation
In progress
### Use study iterative ML used to update the ML model
Not started
### Use study interactive ML in kombination with iterative ML
Not Started
### Use study MT, interactive ML and iterative ML
Not started

### Personas
For initial evaluation regarding the journey predictions we have created three  personas and some scenarios for these personas to help us recreate and simulate situations. The personas and scenarios are presented below. For each user labelled data has been created that matches the users travel patterns. This data differs from real world data in the sense that it only contains valid searches and no [erroneous data](#Data_collection_and_creation).
We have created idealised data that will help us evaluate oru approach, the data has been created using the app so the data mimics a real world situation as close as possible. We have used an interface that

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

### Data collection and creation
Our real world data that currently collect from usage contains irrellevant searches this is due to the constuction of the [app](https://skanependlaren.firebaseapp.com/) and the usage. Example of invalid data coming from the interaction design, is the two dropdowns and the related searches. Searches are done directly when the user changes one of them there therefor is no way to tell if you plan to change both origin and destination or if you are satisfied when you changed only one of them. That is a preferred behaviour since we want to deliver departure times in an efficient way. At the moment we do not have an algorithm that filters searches and tries to find the one that is relevant, this can probably be done but at this stage we have selected to prioritise a functioning ML-algorithm since this will influence all development in the future. The selection of ML algorithm will influence the amount of data cleaning we have to do. There are also situations where a user explores possible routes whithout the intention of conducting them even in the near future, this adds irrelevant data. Our focus at this stage is not on an iterative ML setting instead we focus on the.


## Skånependlaren app
The app that has been used for this work can be downloaded from google play [Skånependlaren](https://skanependlaren.firebaseapp.com/)


<hr>
Images on the pages are owned by the author or if stated otherwise collected from [pixabay](https://pixabay.com) and licenced under [CC0 Creative Commons]( https://creativecommons.org/publicdomain/zero/1.0/deed.en)
_References_

[1] P. Y. Simard et al., “Machine Teaching: A New Paradigm for Building Machine Learning Systems,” 2017.

[2] P. Stappers and E. Giaccardi, “Research through Design,” Encycl. Human-Computer Interact. 2nd ed.; Idea Gr. Ref. Hershey, PA, USA, pp. 1–94, 2017.
