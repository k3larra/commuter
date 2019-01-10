# Usability test plan Commuter
*App version:* 2.1.97<br>
*Test version:* 0.8<br>
*Hardware:* Test users need Android phones with at least sdk version 16 (Jelly Bean) and a data plan.<br>
*Server side:* Running cloud computer 0.5$/h ????<br>
*Costs total:*<br>
*Test time:* 2 weeks<br>
*Number of testers:* 5-10<br>
*Planned start date:* (Need to do some programming first…….1 week work depending on…..)
## Overview
In this initial test we are interested in insightful feedback from users that understands the challenges and opportunities in our design space.  By selecting this approach the users will be able to see through glitches in the design and hopefully be able to contribute to a larger picture.
### Metrics
In this initial use test, our central metric interest is in accuracy of journey predictions after an initial Machine Teaching session. The MT session is designed so the users can add new teaching data, retrain the model and delete all saved data and restart from scratch. The UI used for this and for presenting the predictions can be seen in Figure 1. A video of a journey prediction is visible on [this page]( https://skanependlaren.firebaseapp.com/). Other metrics that we are interested in are feedback around are response time and training time. Response time is the time the user has to wait for a prediction after the app is brought in focus on the smartphone and training time is the time to train a model. Accuracy and response time are at this stage thought as being the most important measurable metrics. The above metrics will be evaluated using a combination of interview questions and logged data.
![Backend](../images/small_prediction.png)
![Backend](../images/trainingdata.png)
**Figure 1:** *In the second figure the app has received a contextbased prediction and departure times has been collected from the transport provider. In the figure on the right the Machine Teaching UI is visible.*
### Usability
In semi structured interviews, that will follow after the test, we are interested in feedback concretely around the teaching UI and ideas around how this UI should be designed for a better experience. We are also interested in the users experience in general in for example these directions:
- Feel of control regarding the training.
- Understanding and transparency of the predictions in relation to the training.
- Would a product like this change your commuting experience in the long term?
- Would it be preferable to learn only interactively?
- Would it be preferable to explicitly save searches as teaching data and avoid a teaching session, train as you go?
- Would it be preferable to hide training and do everything in the background?
- How should a UI that explains the learned data be designed?
- How could a UI that let users edit teaching data be designed?
- More fewer training parameters?
- General feedback.
- General reflections on ML/AI in relation to this experience.
## User demography
To be able to get relevant and insightful response on the issues outlined above we will recruit users with an interaction design background that are well aware of the challenges on different levels when designing for this design space. We will strive for a representative users group but the majority will probably be below 30 years old.  One delimitation is that the users has to commute and should use and own an Android phone.
 ## Ethics and ethical approval.
A contract outlining data collected and further use of this data will be produced and signed by the participants. Need for general ethical approval will be investigated.
## Test plan
In a pure use evaluation, it could be preferable to let the users download the app and start using it on their own. In this case we have and additional interest in a metadiscussion concerning the design. We will therefor introduce the users and get them started in the app usage. This also gives us an opportunity to identify problems related to the user’s model of smartphone and other unforeseen issues.
### Test preparation
User will be informed in a physical meeting regarding the goal of the project get them started to train the app to make predictions. The initial teaching is then erased and the user starts an MT session and trains the app to predict his/her commute patterns.
### Test execution
The users uses the app during a period of max 2 weeks or shorter depending on their experience. The users are expected to use the app, as they would normally do if they downloaded it themselves. Logging of the usage will be done in the background.
### Test termination
When the users finish the test, a semi-structured interview will take place to collect the users experience in the directions outlined in the overview above.
### Data saved in the background.
Data that will be logged is:
-	General use pattern (app start, fragments shown, etc).
-	Predictions made.
-	Teaching data added.
-	Response time for prediction.
-	Retraining done.
-	Reset/delete.
-	Journey searches.

[BACK](../README.md)
