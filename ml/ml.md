## About ml

#### Verification of ML functionality
The focus is not only on optimising the ML algorithm used, of course we want to have accurate predictions, but there are other parameters that has to be taken into account as for example.
* Ease of use
* Generabizability of the algorithm so it can handle a varying amount of data, concept drift and different of use patterns.
* Online inference
* Scalability so each user can have her/his own model.
In our experimentation we did initially work with [tensorflow](https://www.tensorflow.org) and tried out different ML algorithms by using [estimators](https://www.tensorflow.org/guide/estimators). Given our data and our competence in the area these solutions took a lot of time especially in handling with normalisation of parameters tuning and saving the models correctly so inference could be made online. In parallel we evaluated [Fastai](https://www.fast.ai/) framework that builds on [PyTorch](https://pytorch.org/) and found that the abstraction level that framework represents was more in line with our needs. The evaluations below uses Pytorch 1.0 and Fastai 1.0.

Our initial tests with fastai [tabular learner](https://docs.fast.ai/tabular.html) and a neural network with [two hidden layers](ml/baseline.ipynb) gave us predictions that met our expectations regarding accuracy. To evaluate this in a more structured way we created some idealised data using our [personas](#Personas) and senarios. The data was created using our app and the result of the evaluation can be seen in Figure 3 and more details and discussion exists in the persona descriptions.
