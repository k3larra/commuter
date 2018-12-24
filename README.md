# Exploring Machine Learning in a commuting context.
*In this project we explore in what way Machine Learning (ML) can be used to [personalize](#individual-approach-security-and-privacy) and improve performance in a commuter app using some selected contextual parameters (time, day, location and activity). We focus on an interactive approach to Machine Learning (iML) in a series of experiments. We selected commuting and [commute patterns](#Commute-patterns) for our exploration since it is an area that has some characteristics that suits iML well. From a ML perspective training our ML-artifact is an online learning situation that includes cold start, outlier data, data cleaning, concept drift and aging data. In the project we will also study if and how an iML approach changes the user’s notion of ownership both with respect to the training outcome, towards the collected data and the trained model.*

The existing non-ML commuter app [Skånependlaren](https://play.google.com/store/apps/details?id=se.k3larra.alvebuss&hl=sv) focuses on presenting departure times in the commuters near future as efficient as possible. The target group for the app is narrowed to commuters and there is no interface in the app for planning, buying tickets or other more high-level functions.

### Commute patterns
A commuter´s journey pattern are relatively unique for the individual user. Since we focus on journeys that consists of origin destination, and not on predicting only the departure station, it would be difficult to predict a user’s next journey. Therefore, we find the commute context to be an interesting area for researching an individual approach to machine learning.

### Individual approach, security and privacy
Since one of our research interest is around how Machine Learning (ML) can be personalized the focus, in this research, is on the individual experience and not so much the comparison with other users or using other commuters data. Another factor that is important to us is that, even if we handle personal data, travel patterns are private data but cannot be classified on its own as sensitive personal data. In this work, we try to mitigate any privacy issues and [avoid saving data](https://skanependlaren.firebaseapp.com) that can be used to identify individuals. We use standard cloud service security to provide reasonable protection from a security perspetive. We give the users an option to delete all collected data and trained models at any time.

#### Personas
As a complement to the [noisy data](#Data-collection) that our real world users create we have used personas that represents some typical users, one university student, one high school student and one pensioner. These personas together with individual scenarios are used when we our functionality and they also provides best case scenarios. For each persona labelled data has been created that matches the users travel patterns.

* [Maria](personas/Maria.md)
* [Björn](personas/Bjorn.md)
* [Andrea](personas/Andrea.md)

### Data collection
The [app](https://skanependlaren.firebaseapp.com/) creates, from an ML perspective, noisy data due design and usage. Example of noisy data originates from the users interaction with the two dropdowns at the top where origin destination for the journey is selected. Searches are done directly when the user changes one of them, therefor there is no way to tell if you plan to change both origin and destination or if you are satisfied when you changed only one of them. In our design, it is an preferred behaviour since we want to deliver departure times in an efficient way for the user. An example of noisy data that the usage creates are situations where a user explores possible routes for other travellers without the intention of conducting them.

### Methodology
In this project, we use a Research through Design<sup>2</sup> methodology and this site with its history represents our documentation of the explorative process.

### Machine Learning approaches
In this work, we research different levels of human involvement in machine learning. As a simplification there is a decreasing human involvement from Machine Teaching (MT)<sup>1</sup> over interactive ML to more traditional ML. In a Machine Teaching (MT)<sup>1</sup> the users task is to select a minimal set of data that optimizes learning for the ML-artifact. If, as in our case, the commuter knows his/her travel patterns an MT session can be used to overcome situations where no or incorrect data exists for the ML-artifact to learn from. In interactive ML the human user can interact with the ML-artifact, during use, to for example correct false predictions. In our case, this can be used to give feedback to journey predictions or explicitly save new journey predictions. Machine Learning can also take place without user involvement in the background. For our context, we need to iteratively retrain our ML model so it adapts to new travel patterns and in some situations be able to outdated commute patterns. 

### Project plan.
Initially in this project we will focus on the commuters first encounter with the app and the task of training an ML-model so the app can make predictions for her/his recurrent journeys. In the following stages, we will explore a more iterative way of machine learning during usage. At a later stage we will evaluate machine learning that take place in the background, so the model can be trained iteratively during use, even when the user is not aware of it.

The pages referenced below represents the steps of our research in a chronological order:
* [ML backend](backend/backend.md) (Done)
  * [Verification of backend_functionality](backend/backend.md#Verification-of-backend-functionality) (Done)
* [Machine Teaching approach](#Initial-MT-research-approach) (Ongoing)
  * [Verification of ML functionality](#Verification_of_ML_functionality) (Ongoing)
  * [Evaluation of simple MT interface](#Evaluation_of_MT_interface) (Ongoing)
  * [Use study: MT approach handling cold start situation](#User_study_MT_approach_handling_cold_start_situation) (Ongoing)
  * Use study: MT approach updating a trained model
* Interactive ML
* Iterative ML
* Combining MT, interactive ML and iterative ML

<hr>
The app used for this work can be downloaded from google play [Skånependlaren](https://skanependlaren.firebaseapp.com/) <br/>
Some general information around the project can be found [on this site](https://skanependlaren.firebaseapp.com/). The target group for this site is to give app users more information around the project and the ML-artifact. Users will at a later stage be able to log in and inspect their data and trained model.<br/>
Images on the pages are owned by the author or if stated otherwise collected from [pixabay](https://pixabay.com) and licenced under [CC0 Creative Commons]( https://creativecommons.org/publicdomain/zero/1.0/deed.en)<br/>
_References_<br/>
[1] P. Y. Simard et al., “Machine Teaching: A New Paradigm for Building Machine Learning Systems,” 2017.<br/>
[2] P. Stappers and E. Giaccardi, “Research through Design,” Encycl. Human-Computer Interact. 2nd ed.; Idea Gr. Ref. Hershey, PA, USA, pp. 1–94, 2017.
