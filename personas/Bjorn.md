## Fictive persona Björn
_Name:_ Björn<br/>
_Age:_ 69<br/>
_Sex:_ Male<br/>
_Occupation:_ Retired Former plummer<br/>
_Lives:_ Malmö Ön<br/>
_Travel Pattern:_ Recurrent<br/>
_ID:_ hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2<br/>

![Bjorn](images/Bjorn.jpg)

Björn lives in a 3 room apartment on sixth floor near the coast in Malmö. Björn recently got a first grandchild Kim. Kim’s parents Max and Sofia lives in Bunkeflostrand and  Björn picks up Kim from day-care latest 14:00 Tuesday to Friday and walks home to his sons house in Bunkeflo. He stays there until Max or Sofia comes home around 18 and then usually takes the bus home around 19. It is important to Björn to be in time to pick up Kim so he often leaves early and checks the app frequently before he leaves home for delays.
Björn regularly every Saturday afternoon meets his plumber friends Jörgen and Håkan for Boule. They usually meet at Björns place and in central Malmö and walks down to Limhamnsfältet for their boule session. He usually takes the bus home sometime after 18.

### Training and validation set for the first two weeks of usage.
This travel [data](https://github.com/k3larra/commuter/blob/master/data/hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2_start14days.csv) is created using the Björn persona, the data represents the two first weeks of app use use. The usage starts on a Saturday and envisioned searches are added for the coming days and placed in chronological order.

### Training and validation set for the first year of usage.
Travel [data](https://github.com/k3larra/commuter/blob/master/data/hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2_train_valid.csv) estimates the first year of app usage, the data is not in chronological order. The data is create in batches for example one batch represents Monday app searches from Bjorns home in Malmö and his grandchildrens daycare in Bunkeflo, the batches are in this case distibuted over an area around the departure station (200m), over a timespan between 11 and 14 and the activites includes still and walking.

### Teaching sets
One [minimal teaching](https://github.com/k3larra/commuter/blob/master/data/hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2_teaching_set_minimal.csv) set contains one journey representing back and fort to daycare and one representing the saturday meeing with friends. [Another teaching set](https://github.com/k3larra/commuter/blob/master/data/hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2_teaching_set.csv) contains more complete teaching data and is created by adding one row for each day and som for the saturday trip. The added rows matches the travel pattens for Björn.

### Test set
The test data is extracted from the same distribution as the training and validation set for the first year of [use](https://github.com/k3larra/commuter/blob/master/data/hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2_train_valid.csv). The [test set](https://github.com/k3larra/commuter/blob/master/data/hCWCulj7M1aMVyd0Fm0Eqrv8q1Q2_test.csv) consits of 242 rows. This set contains a majority of data reflecting Björns recurrent travel patterns to and from school and uincludes outilier data created mostly over the weekends when she goes to different places in the region.

## Iterative learning camparison.
Using the following code we have evaluated our machine lerning algorithm on Björns data.
![Andrea](https://github.com/k3larra/commuter/raw/master/images/BjornTraining.png)

**Figure 1:** *This figure shows training accuracy during the two first weeks of use, starting from a Saturday. All trained models accuracy are evaluated using the same test set (se above). The blue line represents a Cold Start situation when no data exists to train from. Since the training start on a Saturday only outilier data is aviable to train from and it is not untill the Monday on day 3 that the model reaches around 95% accuracy. This is a consequence of the fact that the journeys on weekdays represents a majority of Björns total journeys. The red line represents a more traditional ML setting were relevant training data is aviable before the model is deployed and used, in this case the data described above from one year of usage is used for the training. The green and orange lines represents a situaion were a teaching set (se above) is added in advance. For the green line only 4 rows exists in the teaching set, and for the orange line 20 rows exists.*

### Scenario 1
It is Wednesday and 12 and Björn checks the add Skånependlaren going from the station "Malmö Ön" to "Bunkeflostrand Centrum". There are no significant delays so Björn decides to take the bus that departs 13:14 and arrives at the destination "Bunkeflostrand Centrum" at 13:27 so he can arrive well in advance to pick up Kim before 14:00.Björn eats lunch and checks the app regularly so no delay or changes appears.

### Scenario 2
It is Saturday morning and Björn calls Jörgen, they decide to start playing boule around 15 when the weather forecast seems suitable. He checks the app at 14 and decides to take the bus from "Malmö Ön" to "Sergels väg" at 14:21. After leaving his apartment at 14:10 he checks for delays a few times while walking to the bus stop.

### Scenario 3
It is Wednesday evening at 19:25 after visiting Kim, Max and Sofia, Björn walks towards the bus stop. Since the buses leaves quite often he has not bothered to check for exact time when the bus leaves. He brings up his app and sees that it leaves in 4 minutes and speeds up his walk to arrive at the bus stop at a convenient time.

<!-- ### Predictions for the scenarios (Not finalized)
* [Predictions after one week use](Bjorn_week.ipynb)
* [Predictions after one month use](Bjorn_month.ipynb)
* [Predictions after one year use](Bjorn_year.ipynb) -->

*Image from Pixabay*

[BACK](README.md)
