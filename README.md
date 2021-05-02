# Spam-Classifier
In this repository i will show you how i did Spam Classifier with Naive Bayes classifier

Github link to repository: https://github.com/MadoDoctor/Spam-Classifier

In this Machine Learning we worked with packages:

* NumPy;
* Pandas;
* re.

<img src="https://latex.codecogs.com/svg.image?\mathbf{P(w_i{|spam})=\frac{N_{spam}(w_1)&plus;\alpha}{N_{spam}&plus;\alpha\times&space;N_{Voc}}" title="\mathbf{P(w_i{|spam})=\frac{N_{spam}(w_1)+\alpha}{N_{spam}+\alpha\times N_{Voc}}" />


<img src="https://latex.codecogs.com/svg.image?\mathbf{N_{spam}(w_i)}" title="\mathbf{N_{spam}(w_i)}" /> - The number of <img src="https://latex.codecogs.com/svg.image?\mathbf{w_i}" title="\mathbf{w_i}" /> words repeated in **spam** messages.

<img src="https://latex.codecogs.com/svg.image?\mathbf{N_{spam}}" title="\mathbf{N_{spam}}" /> - Total number of words in **spam** messages.

<img src="https://latex.codecogs.com/svg.image?\mathbf{N_{Voc}}" title="\mathbf{N_{Voc}}" /> - The total number of unique words in **all** messages.

<img src="https://latex.codecogs.com/svg.image?\mathbf{\alpha}" title="\mathbf{\alpha}" /> - Anti-aliasing parameter
