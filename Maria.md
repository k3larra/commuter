## Fictive persona Maria
Name: Maria

Age: 23

Sex: Female

Occupation: Student (Game design first year, Bachelor level)

Lives: Lund

Travel Pattern: Semirecurrent

![Maria](https://github.com/k3larra/commuter/raw/master/images/Maria321.jpg)

Maria lives by herself at a student accommodation in the City of Lund 10 minutes walk from the train station Lund C. She started studying literature in Lund for one year but felt that this was not really for her; instead, she chose to try if a bachelor program in Game Design at Malmö University could be something for her. She likes playing computer games with a strong narrative and the interdisciplinary aspect of the game design field intrigues her.  She is a thorough student that works hard, spends a lot of time at the University and follows all lectures.  She travels between the stations Lund C and Malmö C in the mornings most weekdays between 8 and 10 and travels in the other direction sometime after 15 in the afternoon.

Marias parent’s lives in a City called Kristianstad and she visits them quite a lot to walk with their dog “Krys” and play computer games with friends and with her younger brother.  Maria travels to Kristianstad around two weeks a month and usually leaves Lund before noon on Saturdays and travels to Kristianstad C. She usual goes back to Lund on the Sunday sometime after 18.

On her spare time, Maria dances Tango and goes out to music pubs mostly in Malmö, for both activities she travels in the evening from the station Lund C to the station Malmö Triangeln and back later the same day.

Maria never remember departure times and uses the app Skånependlaren to check when the next transport leaves. This works well since the times she travels the transport leaves frequently.

Marias collected data can be viewed [here](data/tnK534JMwwfhvUEycn69HPbhqkt2.csv)

And a visualisation of some of the data [here](Maria_dataview.ipynb).

### Scenario 1
It is Monday morning 9:45 and Maria is a little bit late for her lecture 10:15 and checks her app while walking to the station. She expects to get information when the next train leaves and if she needs to run to catch the train.

```
#rows used to predict this journey
#Activity,geoHash,minuteOfDay,weekday
{7,1242479403,531,2}
#Activity 7 walking
#GeoHash around Lund C (124247900-12424800)
#Time 480-600
#Weekday 1-5
#expected result 8121680000 (From station Lund C(81216) to Malmö C(80000)
```

### Scenario 2
It is Saturday morning and Maria wakes up with a headache and decides to go home to her parents in Kristianstad to get some fresh air with her dog. While in bed, she checks her app so she doesn’t need to hurry to catch a suitable train
```
#rows used to predict this journey
#Activity,geoHash,minuteOfDay,weekday
{3,1242479403,560,6}
#Activity 3 still
#GeoHash around Lund C (124247000-124248000)
#Time 540-720
#Weekday 6
#expected result 8121690042 (From station Lund C(81216) to Kristianstad C(90042)
```
### Scenario 3
Maria has spent a late Friday night in Malmö and want information on when the next transport leaves.

```
#rows used to predict this journey
#Activity,geoHash,minuteOfDay,weekday
{7,1242212679,1347,5}
#Activity 7 walking or 3 still
#GeoHash around Malmö Triangeln (1242212000-1242213000)
#Time 1100-1440
#Weekday 5
#expected result 8014081216 (From station Malmö Triangeln(80140) to Lund C(81216)
```

*Image from Pixabay*

[BACK](README.md)
