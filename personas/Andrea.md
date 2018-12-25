# Persona Andrea
_Name:_ Andrea<br/>
_Age:_ 17<br/>
_Sex:_ Female<br/>
_Occupation:_ First year at secondary school with aesthetic focus.<br/>
_Lives:_ Veberöd<br/>
_Travel Pattern:_ Commuter with more random travel patterns on weekends.
_ID:_ ehaBtfOPDNZjzy1MEvjQmGo4Zv12<br/>

![Andrea](https://github.com/k3larra/commuter/raw/master/images/Andrea.jpg)

Andrea lives with her parents in a small village outside Lund called Veberöd. She attends her school in Lund most weekdays. She leaves from the station Veberöd Försköningen" and goes of at the bus stop "Bankgatan" in Lund when she is on her way to school. At irregular times on weekends she travels with friends or alone to Malmö or Lund to shop or just hang out in town.

### Training and validation set for the first two weeks of usage.
This travel [data](https://github.com/k3larra/commuter/blob/master/data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_start14days.csv) is created using the Andrea persona, the data represents the two first weeks of app use use. The usage starts on a Saturday and envisioned searches are added for the coming days and placed in chronological order.

### Training and validation set for the first year of usage.
Travel [data](https://github.com/k3larra/commuter/blob/master/data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_train_valid.csv) estimates the first year of app usage, the data is not in chronological order. The data is create in batches for example one batch represents Monday app searches from Andreas home in Dalby and school in Lunds, the batches are in this case distibuted over an area around the departure station (200m), over a timespan between 7 and 9 in the morning and the activites includes still, walking and running.

### Teaching sets
One [minimal teaching](https://github.com/k3larra/commuter/blob/master/data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_teaching_set_minimal.csv) set contains one morning journey from Veberöd to Lund and one in the opposit direction in the afternoon (those journeys represents around 90% of Andreas travelling). [Another teaching set](https://github.com/k3larra/commuter/blob/master/data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_teaching_set.csv) contains more complete teaching data and is created by adding one row for each day and guessing some destinations for the weekend. The added rows matches the travel pattens for Andrea. For example training data for Monday mornings journeys between Veberöd to Lund, rows are added that representing different activities (still, walking, running), the time is selected in the middle of the timespan.

### Test set
The data is extracted from the same distribution as the training and validation set for the first year of [use](https://github.com/k3larra/commuter/blob/master/data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_train_valid.csv). The [test set](https://github.com/k3larra/commuter/blob/master/data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_test.csv) consits of 379 rows. This set contains a majority of data reflecting Andreas recurrent travel patterns to and from school and uincludes outilier data created mostly over the weekends when she goes to different places in the region.

## Iterative learning camparison.
Using the following code we have evaluated our machine lerning algorithm on Andreas data.
![Andrea](https://github.com/k3larra/commuter/raw/master/images/AndreaTraining.png)

**Figure 1:** *This figure shows training accuracy during the two first weeks of use, starting from a Saturday. All trained models accuracy are evaluated using the same test set (se above). The blue line represents a Cold Start situation when no data exists to train from. Since the training start on a Saturday only outilier data is aviable to train from and it is not untill the Monday on day 3 that the model reaches around 90% accuracy. This is a consequence of the fact that the journeys on weekdays represents around 90% of Andreas total journeys. The red line represents a more traditional ML setting were relevant training data is aviable before the model is deployed and used, in this case the data described above from one year of usage is used for the training. The green and orange lines represents a situaion were a teaching set (se above) is added in advance. For the green line only 2 rows exists in the teaching set, and for the orange line 37 rows exists. It is interesting to note that the minimal teaching set generalise better in the beginning than the more verbose teaching set*

### Scenario 1
It is Monday morning 7:23 and Andrea is as usual late for the bus and runs towards the bus stop "Veberöd försköningen". She checks the app while running to see if there are any delays.

### Scenario 2
It is Saturday 12:23 and Andrea has decided to go to Nova Lund for shopping. She opens up the app and searches for the next departure.

### Scenario 3
In school a Monday 14:50 Andrea checks the app to check next departure and if she needs to hurry to the bus.


### Two weeks usage
This data represents 2 weeks of usage of the app, the data is in chronological order.
[Two weeks data](../data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12start14days.csv)

### One year Data
This data represents an estimation of one years usage, the data is not in chronological order.
[One year data](../data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_train_valid.csv)

### Test set
This data can be used as test set and comes from the same distribution as the one year data. The data is not in chronological order.
[Test set](https://github.com/k3larra/commuter/blob/master/data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_test.csv)

### Teaching set
This data represents travel patterns created using the persona.
[Teaching data minimal](https://github.com/k3larra/commuter/blob/master/data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_teaching_set_minimal.csv)
[Teaching data verbose](https://github.com/k3larra/commuter/blob/master/data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_teaching_set.csv)

### Data visualisation
<!-- * [Predictions after one week use](Andrea_week.ipynb)
* [Predictions after one month use](Andrea_month.ipynb)
* [Predictions after one year use](Andrea_year.ipynb) -->

*Image from Pixabay*

[BACK](README.md)
