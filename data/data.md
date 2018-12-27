# Data creation and data preprocessing.
The Android app used in this project predicts journeys based on individual context-dependent data, the data is used for training an ML-artifact and predict journeys using the ML-artifact. For the predictions, we selected weekday, time of day, location and activity as contextual parameters.
* [App om Google play](https://play.google.com/store/apps/details?id=se.k3larra.alvebuss&hl=sv)
* [App description](https://skanependlaren.firebaseapp.com/)

### "Raw" data
Data created by the app before preprocessing has a format as shown in Figure 1.
![](../images/bqdata.png)
**Figure 1:** *Data before preprocessing*
* detectedActivity is [activity](https://developers.google.com/android/reference/com/google/android/gms/location/DetectedActivity) given by the Android device.
* startStation and endStation are unique numbers given by [Skånetrafiken Open API](http://labs.skanetrafiken.se/api.asp).
* longitude and latitude is position given by the device.
* time is unix timestamp.
* [uid](https://firebase.google.com/docs/auth/android/anonymous-auth) is a unique id connected to the device and the current app installation. This uid is in our application not connected to any user data only to the installation and is created when the app connects to [firebase](https://firebase.google.com/) for the first time.

### Preprocessed data
The data above is preprocessed in the app so it can be used for training an ML-artifacts and do journey predictions. To be able to perform journey classification origin destination is combied to one label. Regarding time our interest is in finding patterns in time of day and weekday therefore our timestamp is converted to weekday and timeOfDay. To handle location close to each other longitude and latitude is combined to one number so nearby places are [numerically close](https://en.wikipedia.org/wiki/Geohash) using a geoHash algorithm.

After the preprocessing the data looks like the figure below.
![](../images/preprocessed_data.png)
* detectedActivity [activity](https://developers.google.com/android/reference/com/google/android/gms/location/DetectedActivity) given by the Android device. The numbers has the following meaning
  * 0 : IN_VEHICLE
  * 1 : ON_BICYCLE
  * 2 : ON_FOOT
  * 3 : STILL
  * 4 : UNKNOWN
  * 5 : TILTING
  * 7 : WALKING
  * 8 : RUNNING
* geoHash is longitude and latitude combined
* startStation and endStation are unique numbers given by [Skånetrafiken Open API](http://labs.skanetrafiken.se/api.asp)
* minuteOfDay represents minutes since midnight
* weekday from 0 to 6 where 0 is Sunday
* journey is the numbers for origin-destination combined as one longer string.

For training detectedActivity and weekday are treated as categorical input parameters and geoHash and minuteOfDay as continous input parameters. The parameters are normalised prior to training.<!--Kolla om detta gäller cat pars-->

### Data sets created for the personas
The datasets created for the personas has been created using the app and the UI seen in the figure below.

![](../images/trainingdatasmall.png)

Using this UI one it is possible to:
* Add one up to 500 labelled training rows in a bulk
* Rows are randomly and evenly place in a circle around a location
* Location for the search can either be the departure station or the location for the device.
* Time is either current time or randomly and evenly distributed over a timespan
* Weekday is either a selected day or evenly distibuted over the week
* Activity is either a selected activity or evenly distributed over activities

By using this UI realistic datasets can be created rather effectively that can serve as training, validation,test and teaching sets for the the personas.
