# Exploring Machine Learning in a commuting context.
*In this project we explore in what way Machine Learning (ML) can be used to personalize and improve performance in a commuter app using contextual parameters (time, day, location and activity). We focus on an interactive approach to Machine Learning (iML) in a series of experiments. We selected commuting and [commute patterns](#Commute_patterns) since it is an area that has some characteristics that suits iML well; especially the fact that it is hard to deduce one users commute patterns from other users. From a ML perspective training our ML-artifact is an online learning situation that includes cold start, outlier data, data cleaning, concept drift and aging data. In the project we will also study if and how an iML approach changes the users feeling of ownership both with respect to the training and to the collected data.*

The existing non ML commuter app [Skånependlaren](https://play.google.com/store/apps/details?id=se.k3larra.alvebuss&hl=sv) focuses on presenting departure times in the near future as efficient as possible. The target group for the app is commuters and consequently there is no interface in the app for planning, buying tickets or other more high level functions. The situation targeted in the original app is getting departure times from a few hours before departure until departure. The [app](https://play.google.com/store/apps/details?id=se.k3larra.alvebuss&hl=sv) as existed prior to this project and delivers departure times including delays, first change of transprot etc.

In this project extension we explore in what way Machine Learning (ML) can be used to personalize and improve performance in the app using contextual parameters (time, day, location and activity). We focus on an interactive approach to Machine Learning (iML) and Machine Teaching (MT)<sup>1</sup> in a series of experiments. We have selected commuting and commute patterns since it is an area that has some characteristics that suits iML well; not very sensitive personal information and that it is hard to deduce one users commute patterns from other users. From a ML perspective training our ML-artifact is an online learning situation that includes cold start, outlier data, data cleaning, concept drift and aging data. In the project we will also study if and how a iML approach changes the users feeling of ownership both with respect to the training and towards the trained ML-model.

The existing non ML commuter app Skånependlaren focuses on presenting departure times in the near future as efficient as possible. The target group for the app is commuters and consequently there is no interface in the app for planning, buying tickets or other more high level functions. The situation targeted is delivering departure times as efficient as possible from a few hours before departure until departure. The app as it has existed prior to this project delivers departure times including delays, first change in transportaion mode and total travel time for the journey, mode and total travel time for the journey.

### Commute patterns
A commuters journey pattern are relativelly unique for the individual user. Since we focus on journeys that consists of origin destination and not on predictiong only the departure station it would be difficult to predict a users next journey except as a guessing based on statistical travel data that predict most common journeys for all travelers in a given situation.

### Individual approach
Since one of our research interest is around how Machine Learning(ML) can be personalized the focus in this research is on the individual experience and not so much the comparison with other users or using other commuters data. The context of commuting fits well into those research interests. Another factor that is important to us is that, even if we handle personal data, travel patterns are not very sensitive and can mostly be missued if they can be connected to a person. In this work we [avoid saving data](https://skanependlaren.firebaseapp.com) that can be used to identify individuals. We do also give the users an option to delete all collected data and trained models.

#### Personas
As a contrrolled environment amd complement to user studies we are using personas that represents some typical users, one university student, one high school student and one pensioner. These personas together with individual scenarions are used as idealised users when we evaluate journey predictions our iML approach. For each user labelled data has been created that matches the users travel patterns. This data differs from real world data in the sense that it only contains valid searches and no [noise](#Data_collection_and_creation). The data has been created using the app (figure 3) so the data mimics the data that will be used for inference.

* [Maria](personas/Maria.md)
* [Björn](personas/Bjorn.md)
* [Andrea](personas/Andrea.md)

### Data collection and creation
Our real world data that currently collect from usage contains irrellevant searches this is due to the constuction of the [app](https://skanependlaren.firebaseapp.com/) and the usage. Example of invalid data coming from the interaction design, is the two dropdowns and the related searches. Searches are done directly when the user changes one of them there therefor is no way to tell if you plan to change both origin and destination or if you are satisfied when you changed only one of them. That is a preferred behaviour since we want to deliver departure times in an efficient way. At the moment we do not have an algorithm that filters searches and tries to find the one that is relevant, this can probably be done but at this stage we have selected to prioritise a functioning ML-algorithm since this will influence all development in the future. The selection of ML algorithm will influence the amount of data cleaning we have to do. There are also situations where a user explores possible routes whithout the intention of conducting them even in the near future, this adds irrelevant data. Our focus at this stage is not on an iterative ML setting instead we focus on the.
### Methodology
In this project we use a Research through Design<sup>2</sup> methodology and this site with its history represents our documentation of the explorative process.

### Machine Learning approaches
 We will use a Machine Teaching<sup>1</sup> (MT) approach to mitigate the consequences of this cold start problem.
We beleve that these different aproaches. so the user can add searces and give feedback to the model on correct and incorrect predictions in an interactive manner

### Project plan.
Initially in the project we will focus on the commuters first encounter with the app and the task of training an ML-model so the app can make predictions for her/his recurrent journeys. In the following stage we will explore a more iterative way of learning. Learning can also take place in the background and the model be trained iteratively during use even when the user is not directely aware of it.

The pages referensed below represents the initial steps:
* [ML backend](backend/backend.md)
  * [Verification of backend_functionality](backend/backend.md#Verification-of-backend-functionality)
* [Machine Teaching approach](#Initial-MT-research-approach)
  * [Verification of ML functionality](#Verification_of_ML_functionality)
  * [Evaluation of simple MT interface](#Evaluation_of_MT_interface)
  * [Use study: MT approach handling cold start situation](#User_study_MT_approach_handling_cold_start_situation)
  * Use study: MT approach for updating a trained model
* Use study: iML
* Use study: iterative ML
* Use study: combining MT, iML and iterative ML

<hr>
The app that has been used for this work can be downloaded from google play [Skånependlaren](https://skanependlaren.firebaseapp.com/)
Some general information around the project can be found [on this site](https://skanependlaren.firebaseapp.com/). The terget group for this site is to give app users more information around the project and the ML-artifact. Users will at a later stage be able to logg in and inpsect their data and model.

Images on the pages are owned by the author or if stated otherwise collected from [pixabay](https://pixabay.com) and licenced under [CC0 Creative Commons]( https://creativecommons.org/publicdomain/zero/1.0/deed.en)
_References_

[1] P. Y. Simard et al., “Machine Teaching: A New Paradigm for Building Machine Learning Systems,” 2017.

[2] P. Stappers and E. Giaccardi, “Research through Design,” Encycl. Human-Computer Interact. 2nd ed.; Idea Gr. Ref. Hershey, PA, USA, pp. 1–94, 2017.
