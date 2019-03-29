## [The CoDesign Study](UserStudy/plan.md)
# Exploring Machine Learning in a commuting context.
*In this project we explore in what way Machine Learning (ML) can be used to [personalize](#individual-approach-security-and-privacy) and improve performance in a commuter app using some selected contextual parameters (time, day, location and activity). We use an Human In The Loop (HITL) approach to ML in a series of experiments. We selected commuting and [commute patterns](#Commute-patterns) for our exploration since it is an area that has some characteristics that suits HITL well. From a ML perspective training our ML-artifact is an online iterative learning situation that includes cold start, outlier data, noisy, concept drift, batch learning and outdated training data. In the project we will also study if and how an HITL approach changes the user’s notion of ownership both with respect to the training outcome, towards the collected data and the trained model.*

The existing non-ML commuter app [Skånependlaren](https://play.google.com/store/apps/details?id=se.k3larra.alvebuss&hl=sv) focuses on presenting departure times in the commuters near future as efficient as possible. The target group for the app is narrowed to commuters and there is no interface in the app for planning, buying tickets or other more high-level functions.

### Commute patterns
A commuter´s journey pattern are relatively unique for the individual user. In the work, we focus on predicting journeys consisting of origin-destination for individual users, and not for example on predicting only the departure station based on a commuter’s location and a statistical probability for next station on a journey. Predicting journeys instead of predicting departure stations and destination stations separate makes the predictions more personalised and based on individual commute patterns instead of more general statistically based commute patterns. Given our research interest in personalisation and machine learning, we find the commute context to be an interesting area for researching this approach to machine learning.

### Individual approach, security and privacy
Our research interest is on how Machine Learning (ML) can be personalised, the focus is therefore on exploring and comparing the users individual experience and not so much comparing commuters data or algorithms used. Another factor that is important to us is that, even if we handle personal data <sup>3, Article 4</sup>, the data is not classified as belonging to any special category of personal data <sup>3,article 9</sup>. In this work, we try to mitigate any privacy issues and avoid saving data that can be used to identify individuals (pseudonymisation) <sup>3,Article 4</sup>]. We use standard cloud service security to provide reasonable protection from a security perspective. We give the a possibility to give consent to data gathering and an opportunity to delete all collected data and trained models at any time.

### Personas
As a complement to the [noisy data](#Data-collection) that our real world users create we have used personas that represents some typical users: one university student, one high school student and one pensioner. These personas together with individual scenarios are used when we our functionality and they also provides best case scenarios. For each persona labelled data has been created that matches the users travel patterns.

* [Maria](personas/Maria.md)
* [Andrea](personas/Andrea.md)
* [Björn](personas/Bjorn.md)

### Data collection
The [app](https://skanependlaren.firebaseapp.com/) collects data when a user makes a journey search by selecting origin and destination. The data collected then is: time, location, activity and the journey.  Due to design and usage, the app creates from an ML perspective: noisy data, irrelevant data and outlier data points. Example of noisy data is searches that originates from the users interaction with the two dropdowns at the top where origin destination for the journey is selected. Searches are done directly when the user changes one of them, therefor there is no way to tell if you plan to change both origin and destination or if you are satisfied when you changed only one of them. In our design, it is an preferred behaviour since we want to deliver departure times in an efficient way for the user. An example irrelevant data are situations where a user explores possible routes to help other travellers or to check out possible routes for him- her-self without the intention of conducting them. Outlier data can in our case be exemplified by journey searches that is not part of any recurrent pattern, like a weekend trip to some friends.

### Methodological approach
For this work we use a Research through Design<sup>2</sup> approach. This site, with its history, represents together with our Android app repository our documentation of the iterative and explorative process.

### Machine Learning approaches
In this work, we research different levels of human involvement in machine learning. As a simplification there is a decreasing human involvement from Machine Teaching (MT)<sup>1</sup> over interactive ML and  active learning to supervised learning. In Machine Teaching (MT)<sup>1</sup> the users task is to select a minimal set of data that optimizes learning for the ML-artifact. If, as in our case, the commuter knows his/her travel patterns an MT session can be used to overcome situations where no or incorrect data exists for the ML-artifact to learn from. In interactive ML the human user can interact with the ML-artifact during use. In our case, this can be used to give feedback on journey predictions or explicitly save new journey predictions. I active learning the users task is more focused on giving feedback on prediction. Machine Learning can also take place without user involvement in the background using a labelled data set created during usage of the app.<br/>
For our context, we need to iteratively train our ML model so it adapts to new travel patterns and in some situations be able to remove outdated commute patterns.

### Project plan.
Initially in this project we will focus on the commuters first encounter with the app and the task of training an ML-model so the app can make predictions for her/his recurrent journeys. In the following stage, we will explore an iterative approach to machine learning during usage. At a later stage we will evaluate machine learning that take place in the background.

The pages referenced below represents the steps of our research in a chronological order:
* [ML backend](backend/backend.md) (Done)
  * [Verification of backend_functionality](backend/backend.md#Verification-of-backend-functionality) (Done)
  * [Data creation and data preprocessing](data/data.md) (Done)
  * [Verification of ML functionality](ml/ml.md) (Done)
* [Machine Teaching approach](machine_teaching/mt.md) (Ongoing)
  * [Evaluation MT functionality](machine_teaching/machine_teaching.md) (Done)
  * Evaluation of simple MT interface (Not started)
  * [Use study: MT approach handling cold start situation](machine_teaching/use_study_cold_start.md) (Planning)
  * Use study: MT approach updating a trained model
* Interactive ML
* Iterative ML
* Combining MT, interactive ML and iterative ML
---
The app used for this work can be downloaded from google play [Skånependlaren](https://skanependlaren.firebaseapp.com/) <br>
Some general information around the project can be found [on this site](https://skanependlaren.firebaseapp.com/). The target group for that site is to give app users more information around the project and the ML-artifact.<br>
Images on the pages are owned by the author or if stated otherwise collected from [pixabay](https://pixabay.com) and licenced under [CC0 Creative Commons]( https://creativecommons.org/publicdomain/zero/1.0/deed.en)<br>
_References_<br>
[1] P. Y. Simard et al., “Machine Teaching: A New Paradigm for Building Machine Learning Systems,” 2017.<br>
[2] P. Stappers and E. Giaccardi, “Research through Design,” Encycl. Human-Computer Interact. 2nd ed.; Idea Gr. Ref. Hershey, PA, USA, pp. 1–94, 2017.
[3] GDPR https://eur-lex.europa.eu/legal-content/ENG/TXT/PDF/?uri=CELEX:32016R0679&rid=1
