# Spam-Classifier
In this repository i will show you how i did Spam Classifier with naive Bayes classifier

Github link to repository: https://github.com/MadoDoctor/Spam-Classifier

In this Machine Learning we worked with packages:

* NumPy;
* Pandas;
* re.

# Introduction to naive Bayes classification

In statistics, naive Bayes classifier are a family of simple "probabilistic classifiers" based on applying Bayes' theorem with strong (naïve) independence assumptions between the features. Bayes' theorem is stated mathematically as the following equation:

<img src="https://latex.codecogs.com/svg.image?\mathbf{P(A|B)=\frac{P(B|A)P(A)}{P(B)}}" title="\mathbf{P(A|B)=\frac{P(B|A)P(A)}{P(B)}}" />

<img src="https://latex.codecogs.com/svg.image?\mathbf{P(A|B)}" title="\mathbf{P(A|B)}" /> - is a conditional probability: the probability of event **A** occurring given that **B** is true. It is also called the posterior probability of **A** given **B**.

<img src="https://latex.codecogs.com/svg.image?\mathbf{P(B|A)}" title="\mathbf{P(B|A)}" /> -  is also a conditional probability: the probability of event **B** occurring given that **A** is true. It can also be interpreted as the likelihood of **A** given a fixed **B** because <img src="https://latex.codecogs.com/svg.image?\mathbf{P(B|A)=L(A|B)}" title="\mathbf{P(B|A)=L(A|B)}" />.

<img src="https://latex.codecogs.com/svg.image?\mathbf{P(A)}" title="\mathbf{P(A)}" /> and <img src="https://latex.codecogs.com/svg.image?\mathbf{P(B)}" title="\mathbf{P(B)}" /> are the probabilities of observing **A** and **B** respectively without any given conditions; they are known as the marginal probability or prior probability.

***A*** and **B** must be different events.

<img src="https://latex.codecogs.com/svg.image?\mathbf{P(w_i{|spam})=\frac{N_{spam}(w_1)&plus;\alpha}{N_{spam}&plus;\alpha\times&space;N_{Voc}}" title="\mathbf{P(w_i{|spam})=\frac{N_{spam}(w_1)+\alpha}{N_{spam}+\alpha\times N_{Voc}}" />


<img src="https://latex.codecogs.com/svg.image?\mathbf{N_{spam}(w_i)}" title="\mathbf{N_{spam}(w_i)}" /> - The number of <img src="https://latex.codecogs.com/svg.image?\mathbf{w_i}" title="\mathbf{w_i}" /> words repeated in **spam** messages.

<img src="https://latex.codecogs.com/svg.image?\mathbf{N_{spam}}" title="\mathbf{N_{spam}}" /> - Total number of words in **spam** messages.

<img src="https://latex.codecogs.com/svg.image?\mathbf{N_{Voc}}" title="\mathbf{N_{Voc}}" /> - The total number of unique words in **all** messages.

<img src="https://latex.codecogs.com/svg.image?\mathbf{\alpha}" title="\mathbf{\alpha}" /> - Anti-aliasing parameter.

