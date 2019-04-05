## Week 2 (In progress)
**In this CoDesign study we will together use a design probe and explore the area of Machine Teaching (MT)<sup>1</sup> in a commuting context.**

### Goal for the week
By teaching once in the beginning of the week we will explore a cold start/batch teaching situation for the given context. The idea is that this will give us a perspective of how well the system will perform in relation to the expectations you have on your teaching.
As a consequence we could get insights in howto to answer research questions like these:

1. How does the your expectations, given this implementation, on the teaching match the outcome in a batch teaching situation (Notes.)?
2. How does the perceived performance of the predictions relate to measured performance of the predictions (In seconds as measured by the app, we will evaluate this during next week's meeting but keep it in mind during use)?
3. How could a batch teaching interface be designed for the context (If you have time some sketches would be supergreat :))?

### Background info: Cold start
A general challenge in Machine Learning (ML) is Cold start.
Since ML is all about learning if an ML-model hasn't been taught anything it knows nothing. Depending on the type of type of model it has an ability to learn specific things, like distinguish between car-brands in images.
Think of the ML-model-type (or ML-algorithm) as for example a kitten, it has the ability to be trained in doing cat-stuff like catching and eating birds and with training it will do that well but it will never be able to play piano or bark.

To handle the Cold start problem there are different strategies and two are nd transfer learning and bootstrapping.
* In transfer learning you take a ML-model that has been trained on similar data and add more training data. For example a CNN-model (Recognises images) that has been trained on dog and cat images and you train it to recognize cat breeds like Persian, Coon etc.
* In bootstrapping you add data that is similar to the data you expect to arrive when the model is in use. This is what I do in the commuter app. When you teach it I add 40 labelled (Correct data) spread over the location area, time, weekday and activities that has been selected in the teaching interface. It can look like this [teaching data](https://github.com/k3larra/commuter/blob/master/UserStudy/week2/teach.csv).

### Second week usage: ASSIGNMENT
Think through your weeks commute and teach the app so you think it will be able to predict the journeys. Then during the week **don't** clear teaching and **don't** reteach anything. Instead make an mental note (or real) of how well the app performs in relation to your expectations (The RQ2).

# Feedback
***Add feedback here both general issues and thinking sketches or just so you remember, the more the better. Especially things that relates to the research questions above:***<br/>
### ***https://github.com/k3larra/commuter/issues*** <br/>

***Mail me directly if the app hangs.***


#### You are here page:
https://github.com/k3larra/commuter/blob/master/UserStudy/week2/presentation.md

### References
??<br/>
[1] [P. Y. Simard et al., “Machine Teaching: A New Paradigm for Building Machine Learning Systems,” 2017](https://arxiv.org/pdf/1707.06742v3.pdf).<br/>
[2] [N. Banovic and J. Krumm, “Warming Up to Cold Start Personalization,” PACM Interact. Mob. Wearable Ubiquitous Technol, vol. 1, no. 13, 2017.](Warming_Up.pdf)
