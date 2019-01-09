# Initial MT research approach
[Code](mt.ipynb)

Our focus, in this part of the project, is the users first encounter with the commuter app. In this situation the app has no knowledge of the users commute patterns and cannot make any accurate predictions. The commute patterns could be learned over time but it would take some time and is complicated by [noisy data](../data/data.md). In our approach we are interested in transferring the commuters knowledge of his/her commute patterns to the ML artifact and thus mitigate cold start problem.

Our delimitation is to explore and evaluate a MT approach that starts with an initial Machine Teaching session. During this session the user adds his/her known travel patterns that is used to train the model so journey predictions can be made from start.
The training is done using the same model and settings as in [ml verification](../ml/ml.md)

 In this part of the work, presented on this page, we focus on the models performance for different teaching sets. We do not optimize the model in any way to optimize predictions but keep our initial settings from our [ML verification](../ml/ml.md). We are instead interested in finding and using a model that can handle training sets from different distributions.

 The app version used and the interface used to create teaching data in part 1 can be seen in Figure 1.

![Backend](../images/small_detail_search.png)
![Backend](../images/small_prediction.png)
![Backend](../images/trainingdata.png)

**Figure 1:** *In the figure on the left the standard app is shown and details for one departure is expanded. In the second figure the app has received a contextbased prediction and departure times has been collected from the transport provider. In the figure on the right labelled training data can be added.*

## Part 1: Functional test with teaching data.
To evaluate the approach some teaching sets were created for each user. One minimal with only the most frequent patterns and one more verbose that targeted all scenarios for the persona. In the more verbose set we created data rows from imagining the different combinations of arguments for each journey. The initial teaching sets were created using the UI on the right in figure 1.
<br>**Teachingsets created:**<br>
Andrea:
[Verbose](../data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_teaching_set.csv)
[Limited](../data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_teaching_set_minimal.csv)
<br>Björn:
[Verbose](../data/hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2_teaching_set.csv)
[Limited](../data/hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2_teaching_set_minimal.csv)
<br>Maria:
[Verbose](../data/tnK534JMwwfhvUEycn69HPbhqkt2_teaching_set.csv)
[Limited](../data/tnK534JMwwfhvUEycn69HPbhqkt2_teaching_set_minimal.csv)

To evaluate the models we used the same test sets as in our [ML verification](../ml/ml.md)
<br>**Test sets used:**<br>
[Andrea test set](../data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_test.csv)<br>
[Björn test set](../data/hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2_test.csv)<br>
[Maria test set](../data/tnK534JMwwfhvUEycn69HPbhqkt2_test.csv)

### Results part 1: Training with hand made teaching sets.
The results of the evaluations were mixed and indicates that it is hard to create a good teaching set by hand. To hande the sometimes small teahing sets the rows were duplicated so at least 1000 rows are in the teaching sets. But the results are initially promising as can be seen in Figure 2 and for the individual users in Figure 3-5.

In figure 1 the accuracy for the users journeys in the test sets are shown distributed over the week. For Andrea the results are good since she her travel patterns are regular on weekdays but more irregular on weekends. In her teaching sets her weekend journeys are more correct than in the original data set. For Björn and Maria it becomes clear that the model can't distinguish the important parametes from the ones that does limited information. This indicates that it is important to augment the training data so the parameters that carries less information is more random.

![](../images/andrea_teach1_small.png)
![](../images/bjorn_teach1_small.png)
![](../images/maria_teach1_small.png)

**Figure 2:** *The accuracy and SD for the accuracy distributed over the week for the different users. The models used are trained using the teaching sets and evaluated towards the same test set for each user.*

In the figures below more details around the training for each users is presented.

#### Minimal teaching set
Using the minimal teaching sets for training training results and confusion matrix fpor the personas.

**Andrea**

![](../images/andrea_train2.png)
![](../images/andrea_cf11.png)

**Figure 3:** *For Andrea only her commute patterns to school is in the teaching set as seen in the confusion matrix. The accuracy is acceptable since the bulk of Andreas journeys are to and from school. Accuracy on test set 0.89*

**Björn**

![](../images/bjorn_train1.png)
![](../images/bjorn_cf1.png)

**Figure 3:** *For Björn the result is not acceptable and the journeys are confused with each other. This can also be seen in Figure 1. Accuracy on test set 0.57*

**Maria**

![](../images/maria_train1.png)
![](../images/maria_cf1.png)

**Figure 4:** *For Maria the result can be acceptable the teaching sets includes some of her irregular journeys on the evenings and correctly predicts many of her commutes to school in Malmö. Accuracy on test set 0.86*

### Verbose manual teaching set

**Andrea**

![](../images/andrea_train2.png)
![](../images/andrea_cf2.png)

**Figure 5:** *. Accuracy on test set 0.92*

**Björn**

![](../images/bjorn_train2.png)
![](../images/bjorn_cf2.png)

**Figure 6:** *... Accuracy on test set 0.74*
Accuracy 0.74

**Maria**

![](../images/maria_train2.png)
![](../images/maria_cf2.png)

**Figure 4:** *. Accuracy on test set 0.98*


## Part 2: Augmented teaching set
To overcome some of the limitations in the functional test above a teaching UI is created that automatically augment the data. Data augmentation is generally a way to get more data out of limited data. In our case creating extra data points over a time interval or over multiple locations can give better accuracy [REFS].
The interface in figure 2 was used, the data is agmented in the following way........ss..

![](../images/mt1.png)

<br>Teachingsets created:<br>
Andrea:
[Augmented](../data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_teaching_set_aug.csv)
<br>Björn:
[Augmented](../data/hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2_teaching_set_aug.csv)
<br>Maria:
[Augmented](../data/tnK534JMwwfhvUEycn69HPbhqkt2_teaching_set_aug.csv)

### Andrea

![](../images/andrea_train3.png)
![](../images/andrea_teach3.png)
![](../images/andrea_cf3.png)

Accurracy test set: 0.88

### Björn

![](../images/bjorn_train3.png)
![](../images/bjorn_teach3.png)
![](../images/bjorn_cf3.png)

Accurracy test set: 1.0

### Maria

![](../images/maria_train3.png)
![](../images/maria_teach3.png)
![](../images/maria_cf3.png)

Accurracy test set: 0.99
