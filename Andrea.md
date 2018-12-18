## Fiktive persona Andrea
Name: Andrea

Age: 17

Sex: Female

Occupation: First year at secondary school with aesthetic focus.

Lives: Veberöd

Travel Pattern: Semi-recurrent

![Andrea](https://github.com/k3larra/commuter/raw/master/images/Andrea.jpg)

Andrea lives with her parents in a small village outside Lund called Veberöd. She attends her school in Lund most weekdays. She leaves from the station Veberöd Försköningen" and goes of at the bus stop "Bankgatan" in Lund when she is on her way to school. At irregular times on weekends she travels with friends or alone to Malmö or Lund to shop or just hang out in town.

### Training and validation set for the first two weeks of usage.
Travel [data](https://github.com/k3larra/commuter/blob/master/data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_start14days.csv) outlines the 2 first weeks of use. The usage starts on a Saturday and envisioned searches are added for the coming days.

### Training and validation set for the first year of usage.
Travel [data](https://github.com/k3larra/commuter/blob/master/data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_train_valid.csv) estimates the first year of usage, the data is not in order. The data is create in batches for example one batch represents Monday travels from Andreas home in Dalby and school in Lunds, the batches are distibuted over an area around the departure station, over a timespan between 7 and 9 combied with the activites (stil, walking and running).

### Teaching sets
One [minimal teaching](https://github.com/k3larra/commuter/blob/master/data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_teaching_set_minimal.csv) set contains one morning journey from Veberöd to Lund and one in the opposit direction in the afternoon (that journey represents around 90% of Andreas travelling). [Another teaching set](https://github.com/k3larra/commuter/blob/master/data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_teaching_set.csv) contains more complete teaching data and is created by adding one row for each day and guessing some destinations for the weekend. The added rows matches the travel pattens for Andrea. For example monday morning Veberöd to Lund there are rows added representing different activities (still,walking,running), the time is selected in the middle of the timespan.

### Test set.
The data is extracted from the same distribution as the training and validation set for the first year of use. The [test set](https://github.com/k3larra/commuter/blob/master/data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_test.csv) that consits of 379 rows. This set contains a majority of data reflecting Andreas recurrent travel patterns to and from school and outilier data mostly over the weekends when she goes to different places in the region.

## Machine Learning comparison
![Andrea](https://github.com/k3larra/commuter/raw/master/images/AndreaTraining.jpg)

### Scenario 1
It is Monday morning 7:23 and Andrea is as usual late for the bus and runs towards the bus stop "Veberöd försköningen". She checks the app while running to see if there are any delays.


### Scenario 2
It is Saturday 12:23 and Andrea has decided to go to Nova Lund for shopping. She opens up the app and searches for the next departure.


### Scenario 3
In school a Monday 14:50 Andrea checks the app to check next departure and if she needs to hurry to the bus.


<!-- ### Predictions for the scenarios (Not finalized) -->
<!-- * [Predictions after one week use](Andrea_week.ipynb)
* [Predictions after one month use](Andrea_month.ipynb)
* [Predictions after one year use](Andrea_year.ipynb) -->

*Image from Pixabay*

[BACK](README.md)
