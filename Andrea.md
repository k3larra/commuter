## Fiktive persona Andrea
Name: Andrea

Age: 17

Sex: Female

Occupation: First year at secondary school with aesthetic focus.

Lives: Veberöd

Travel Pattern: Semi-recurrent

![Andrea](https://github.com/k3larra/commuter/raw/master/images/Andrea.jpg)

Andrea lives with her parents in a small village outside Lund called Veberöd. She attends her school in Lund most weekdays. She leaves from the station Veberöd Försköningen" and goes of at the bus stop "Bankgatan" when she is on her way to school. At irregular times on weekends she travels with friends or alone to Malmö or Lund to shop or just hang out in town.

### Training and validation select
Travel [data](https://github.com/k3larra/commuter/blob/master/data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_start14days2.csv) outlines the 2 first weeks of use. The usage starts on a saturday and envisioned searches are added for the coming days.

### Test set.
Data has been generated based on the persona and estimated [for one year of use](https://github.com/k3larra/commuter/blob/master/data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_train_valid.csv) consiting of 3418 rows. The data is randomized with respect to time and is used to select a [test set](https://github.com/k3larra/commuter/blob/master/data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_test.csv) that consits of around ten percent of the rows (379 rows). This set consits of a majority of data that reflect Andreas recurrent travel patterns to and from school and outilier data mostly over the weekends when she goes to different places in the region.

### Usage data for the first 2 weeks.
Travel [data](https://github.com/k3larra/commuter/blob/master/data/ehaBtfOPDNZjzy1MEvjQmGo4Zv12_start14days2.csv) that outlines the 2 first weeks of use. The usage starts on a saturday and envisioned searches are added for the coming days.

### Machine Learning comparison


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
