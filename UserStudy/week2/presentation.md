## Week 2 (In progress)
**In this CoDesign study we will together use a design probe and explore the area of Machine Teaching (MT)<sup>1</sup> in a commuting context.**

### Goal for the week
By teaching once in the beginning of the week we will explore a cold start/batch teaching situation for the given context. The idea is that this will give us a perspective of how well the system will perform in relation to the expectations you have on your teaching.
Therefor we could get insights in how to answer research questions like these:

**RQ1:** How does your expectations, given this implementation, on the teaching match the outcome when the teaching has taken place prior to the usage (batch teaching)?

**RQ2:** How does the perceived performance of the predictions relate to measured performance of the predictions (In seconds as measured by the app, we will evaluate this during next week's meeting but keep it in mind during use)?

**RQ3:** How could a batch teaching interface be designed for the context (If you have time some sketches would be supergreat :))?

### Background info: Cold start
A general challenge in Machine Learning (ML) is Cold start.
Since ML is all about learning if an ML-model hasn't been taught anything it knows nothing. Depending on the type of type of model, it has an ability to learn specific things, like distinguish between objects in images.
Think of the ML-model-type (or ML-algorithm) as for example a kitten, it has the ability to be trained in doing cat-stuff like catching and eating cute birds and with training it will do that well but it will never be able to play piano or bark. It is a similar difference between ML-algorithms like "random forest", "linear regression" or a "CNN (Convolutional Neural Network)", each algorithm works best for a specific type of input data.

To handle the Cold start problem there are different strategies and two are transfer learning and bootstrapping.
* In transfer learning, you take a ML-model that has been trained on similar data and add more training data. For example, a CNN-model (good for images) that has been trained on distinguishing between dog and cat images and you train it to recognize cat breeds like Persian, Coon etc.
* In bootstrapping, you add data that is similar to the data you expect to arrive when the model is in use. This is what I do in the commuter app. When you teach it I add 40 labelled (Correct data) spread over the location area, time, weekday and activities that has been selected in the teaching interface. It can look like this: [teaching data](https://github.com/k3larra/commuter/blob/master/UserStudy/week2/teach.csv).

### Second week usage: "ASSIGNMENT"
Think through your weeks commute and teach the app so you think it will be able to predict the journeys you will do during the week. Then during the week **don't** clear teaching and **don't** reteach anything. Instead, make an note of how well the app performs in relation to your expectations (RQ1).

## Feedback

***Add feedback here both general issues, thoughts and sketches or just notes so you remember, the more the better. Especially things that relates to the research questions above is valuable:***

### ***https://github.com/k3larra/commuter/issues***

#### This page:
https://github.com/k3larra/commuter/blob/master/UserStudy/week2/presentation.md

#### References
[1] [P. Y. Simard et al., “Machine Teaching: A New Paradigm for Building Machine Learning Systems,” 2017](https://arxiv.org/pdf/1707.06742v3.pdf).<br/>
[2] [N. Banovic and J. Krumm, “Warming Up to Cold Start Personalization,” PACM Interact. Mob. Wearable Ubiquitous Technol, vol. 1, no. 13, 2017.](Warming_Up.pdf)
