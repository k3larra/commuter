## Week 2 (In progress)
**In this CoDesign study we will together use a design probe and explore the area of Machine Teaching (MT) in a commuting context.**

### Goal for the week
By teaching once in the beginning of the week we will explore a cold start/batch teaching situation for the given context. The idea is that this will give us a perspective of how well the system will performs in relation to the expectations you have on your teaching when the teaching is done once in the beginning of the week.
As a consequence we could start to answer research questions like these:

* How does the your expectations, given this implementation, on the teaching match the outcome in a batch teaching situation (Notes.)?
* How does the perceived performance relate to measured performance (In seconds we will evaluate that next week but keep it in mind during use)?
* How can a batch teaching interface be designed for the context (If you have time and it is your area some sketches would be super)?

### Cold start
A general challenge in Machine Learning (ML) is Cold start.
Since ML is all about learning if an ML-model hasn't been taught anything it knows nothing. Depending on the type of type of model it has an ability to learn specific things, like distinguish between images.).
Think of the model type as for example a kitten, it has the ability to learn cat-stuff and with training it will do that well but it will never be able to play piano or bark.

To handle the Cold start problem there are different strategies and two are bootstrapping and transfer learning.
* Using transfer learning you take a ML-model that has been trained on similar data and add more training data. For example a CNN-model (Recognises images) that has been trained on dog and cat images and you train it to recognize cat breeds like Persian, Coon etc.
* Using bootstrapping you add data that is similar to the data you expect to arrive. This is what I do in the commuter app. When you teach it I add 40 labelled (Correct data) spread over the location area, time, weekday and activities. It can look like this [teaching data](https://github.com/k3larra/commuter/blob/master/UserStudy/week2/teach.csv).

### Second week usage
Think through your weeks usage and teach the app so you think it should be able to predict the journeys. Then during the week don't reteach anything. Instead make an mental note of how well the app performs in relation to your expectations (The RQ:s).

# Feedback

***Add feedback here both general issues and thinking sketches etc. that relates to the research questions:
https://github.com/k3larra/commuter/issues*** <br/>
***Write everything you think is strange and things that don't work.*** <br/>
***Mail me directly if the app hangs and it doesn't so it can't be used.***


#### This page:
https://github.com/k3larra/commuter/blob/master/UserStudy/week1/presentation.md

### References
[1] Ehn, Pelle, Elisabet M. Nilsson, and Richard Topgaard (eds.). (2014). Making Futures: Marginal Notes on Innovation, Design, and Democracy. MIT Press. (340 p)<br/>
[1] P. Y. Simard et al., “Machine Teaching: A New Paradigm for Building Machine Learning Systems,” 2017.
