# Initial MT research approach

[BACK](../README.md)

[Code](mt.ipynb) used especially in this evaluation.

Our focus, in this part of the project, is the user’s first encounter with the commuter app. In this situation/scenario, the app has no knowledge of the users commute patterns and cannot make any accurate predictions. The commute patterns could be learned over time but it would take some time and is complicated by [noisy data](../README.md#data-collection). In our approach we are interested in transferring the commuters knowledge of his/her commute patterns to the ML artifact and thus mitigate cold start problem.

Described below is an exploration and evaluation of an MT approach that starts with an initial Machine Teaching session. During this session the user adds his/her known travel patterns that will be used to train the model so journey predictions can be made accurately from first use of the app.

 The presentation on this page focus on the models performance for different teaching sets. We do not optimize the model in any way to optimize predictions for the teaching sets instead we keep our initial settings from our [ML verification](../ml/ml.md). We do this to evaluate the models robustness with respect to different distributions of teaching sets.

## Part 1: Functional test with teaching data.

 The app version and the interface used to create teaching data in this part can be seen in Figure 1.

![Backend](../images/small_detail_search.png)
![Backend](../images/small_prediction.png)
![Backend](../images/trainingdata.png)

**Figure 1:** *On the left the standard app is shown and details for one departure is expanded. In the second figure the app has received a contextbased prediction and departure times has been collected from the transport provider. In the figure on the right labelled teaching data can be added.*


To evaluate the approach some teaching sets were created for each user. One minimal set with only the most frequent patterns and one more verbose that targeted all scenarios for the persona. In the more verbose set, we created data rows by imagining the different combinations of arguments for each journey. We created the teaching sets using the UI on the right in figure 1.

**Teachingsets created:**<br>
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

**Test sets used:**<br>
[Andrea test set](../data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_test.csv)<br>
[Björn test set](../data/hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2_test.csv)<br>
[Maria test set](../data/tnK534JMwwfhvUEycn69HPbhqkt2_test.csv)

### Results part 1: Training with hand made teaching sets.
The results of the evaluations were mixed and indicates that it is hard to create a good teaching set by hand. To handle the sometimes small teaching sets the rows were duplicated so at least 1000 rows are in the teaching sets. But the results are initially promising as can be seen in Figure 2 and for the individual users in Figure 3-7.

In Figure 1 the accuracy for the users journeys in the test sets are shown distributed over the week. For Andrea the results are good since she her travel patterns are regular on weekdays but more irregular on weekends. In her teaching sets, her weekend journeys are more correct than in the original data set. For Björn and Maria it becomes clear that the model can't distinguish the parameters with most information gain from the ones that holds limited information. This indicates that it is important to augment the training data so the parameters that carries less information is more random.

![](../images/andrea_teach1_small.png)
![](../images/bjorn_teach1_small.png)
![](../images/maria_teach1_small.png)

**Figure 2:** *The accuracy and SD for the accuracy distributed over a week for the different personas. The models used are trained using the teaching sets and evaluated towards the same test set for each user.*

In the figures below more details around the training result for each users is presented.

#### Minimal teaching set

**Andrea**

![](../images/andrea_train2.png)
![](../images/andrea_cf1.png)

**Figure 3:** *Andrea has only her commute patterns to school in the teaching set as seen in the confusion matrix. The accuracy is acceptable since the bulk of Andreas journeys are to and from school. Accuracy on test set 0.89*

**Björn**

![](../images/bjorn_train1.png)
![](../images/bjorn_cf1.png)

**Figure 3:** *For Björn the result is unclear and the journeys are confused with each other. This can also be seen in Figure 1. Accuracy on test set is 0.57*

**Maria**

![](../images/maria_train1.png)
![](../images/maria_cf1.png)

**Figure 4:** *For Maria the result can be acceptable, the teaching sets includes some of her irregular journeys on the evenings and correctly predicts many of her commutes to school in Malmö. Accuracy on test set 0.86*

#### Verbose teaching set

**Andrea**

![](../images/andrea_train2.png)
![](../images/andrea_cf2.png)

**Figure 5:** *Some of Andreas evening journeys are correctely predicted but since she has no distinct commute pattern, regarding those journeys, it is hard to predict any of them with high accuracy. The total accuracy for the test set is 0.92 since the bulk of journeys are on weekdays to school*

**Björn**

![](../images/bjorn_train2.png)
![](../images/bjorn_cf2.png)

**Figure 6:** *For Björn the result is really mixed and many journeys are confused with each other giving an accuracy on the test set of 0.74.*

**Maria**

![](../images/maria_train2.png)
![](../images/maria_cf2.png)

**Figure 7:** *For Maria the verbose teaching set worked well. Accuracy on test set 0.98*


## Part 2: Augmented teaching set
To overcome some of the limitations in the test above a the teaching UI is transformed so it can be used to create and augment teaching data. The interface for experimental teaching interface can be seen in Figure 8. The data is augmented in the following way:

- The datapoints created are evenly distributed around departure station or smartphone location.
- Time instances distributed over a time span or the whole day.
- Fixed day, weekend, weekday or independant of day.
- Datapoints for one [activity](../data/data.md) or evenly distributed over activities.
- 40 rows, using the distribution outlined above, are created when "ADD TRAINING DATA" is pressed.

Selecting 40 rows is a tradeoff between number of rows and enough augmentation of data. For example Andreas journeys to school in mornings were added by selecting correct origin destination, 400 meters around departure station and a timespan between 07:00 and 09:00 for weekdays.

![](../images/mt10.png)

**Figure 8:** *Experimental teaching interface that creates 40 augmented rows in batches.*

### Results part 2: Training with augmented teaching set.
The results for these teaching sets clearly indicates that the extra amount of data gives the neural network more information to train from and a better possibility to converge on the parameters with most information gain.

Teachingsets created:<br>
Andrea:
[Augmented](../data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_teaching_set_aug.csv)
<br>Björn:
[Augmented](../data/hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2_teaching_set_aug.csv)
<br>Maria:
[Augmented](../data/tnK534JMwwfhvUEycn69HPbhqkt2_teaching_set_aug.csv)

In Figure 9 the accuracy for the users journeys in the test sets are shown distributed over the week. Compared to Figure 2 the augmented teaching set is added and a significant increase in accuracy and a decrease in standard deviation can be observed. Especially the metrix for Björn has improved.

![](../images/andrea_teach3.png)
![](../images/bjorn_teach3.png)
![](../images/maria_teach3.png)

**Figure 9:** *The accuracy and SD for the accuracy distributed over a week for the different personas. The models used are trained using the teaching sets and evaluated towards the same test set for each user.*

In the figures below more details around the training result for each users is presented.

**Andrea**

![](../images/andrea_train3.png)
![](../images/andrea_cf3.png)<br>
**Figure 10:** *Andreas results in parity with preious results, the accuracy on test set decreased compared to the verbose teaching set to 0.88. False positives are due to lack of information regarding iregular weekend journeys.*

**Björn**

![](../images/bjorn_train3.png)
![](../images/bjorn_cf3.png)

**Figure 11:** *For Björn the augmented teaching set helped the model significantly to distinguish his weekend journeys from the weekday journeys. Accuracy on test set 1.0*

**Maria**

![](../images/maria_train3.png)
![](../images/maria_cf3.png)

**Figure 12:** *The augmented teaching set increased the accuracy on test set for Maria to 0.99. So no drastic improvement.*

[BACK](../README.md)
