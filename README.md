# Exploring Machine Learning in a commuting context.
*In this project we explore in what way Machine Learning (ML) can be used to [personalize](individual-approach,-security-and-privacy) and improve performance in a commuter app using some selected contextual parameters (time, day, location and activity). We focus on an interactive approach to Machine Learning (iML) in a series of experiments. We selected commuting and [commute patterns](#Commute-patterns) for our exploration since it is an area that has some characteristics that suits iML well. From a ML perspective training our ML-artifact is an online learning situation that includes cold start, outlier data, data cleaning, concept drift and aging data. In the project we will also study if and how an iML approach changes the users notion of ownership both with respect to the training outcome and towards the collected data.*

The existing non ML commuter app [Skånependlaren](https://play.google.com/store/apps/details?id=se.k3larra.alvebuss&hl=sv) focuses on presenting departure times in the commuters near future as efficient as possible. The target group for the app is narrowed to commuters and consequently there is no interface in the app for planning, buying tickets or other more high level functions.

### Commute patterns
A commuters journey pattern are relativelly unique for the individual user. Since we focus on journeys that consists of origin destination and not on predictiong only the departure station it would be difficult to predict a users next journey except as a guessing based on statistical travel data that predict most common journeys for all travelers in a given situation. Therefore we find the commute context to be an interesting area for researching an individual approch to machine learning.

### Individual approach, security and privacy
Since one of our research interest is around how Machine Learning(ML) can be personalized the focus in this research is on the individual experience and not so much the comparison with other users or using other commuters data. The context of commuting fits well into those research interests. Another factor that is important to us is that, even if we handle personal data, travel patterns are private data but is not the most sensitive personal data. In this work we try to mitigate any privacy issues by [avoiding saving data](https://skanependlaren.firebaseapp.com) that can be used to identify individuals and we use standard cloud service security. We do also give the users an option to delete all collected data and trained models at any time.

#### Personas
As a complement to the often [noisy data](#Data-collection) that real world users create we have used personas that represents some typical users, one university student, one high school student and one pensioner. These personas together with individual scenarions are used when we evaluate journey predictions. For each persona labelled data has been created that matches the users travel patterns.

* [Maria](personas/Maria.md)
* [Björn](personas/Bjorn.md)
* [Andrea](personas/Andrea.md)

### Data collection
Our real world data thatthe app usage created contains some irrelevant searches due to the constuction of the [app](https://skanependlaren.firebaseapp.com/) and the usage. Example of invalid data coming from the design is the two dropdowns at the top. Searches are done directly when the user changes one of them there therefor there is no way to tell if you plan to change both origin and destination or if you are satisfied when you changed only one of them. In our design it is an preferred behaviour since we want to deliver departure times in an efficient way for the user. An example of irellevant searches that the usage create are also situations where a user explores possible routes for other travellers whithout the intention of conducting them even in the near future. 

### Methodology
In this project we use a Research through Design<sup>2</sup> methodology and this site with its history represents our documentation of the explorative process.

### Machine Learning approaches
 We will use a Machine Teaching<sup>1</sup> (MT) approach to mitigate the consequences of this cold start problem.
We beleve that these different aproaches. so the user can add searces and give feedback to the model on correct and incorrect predictions in an interactive manner
and Machine Teaching (MT)<sup>1</sup>

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
