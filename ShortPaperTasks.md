# Short Paper
## Models
### Due: Mar 18, 2025

Groups will submit their implemented models, initial experimental results, 
and describe their planned experimental analysis. This report should add any 
new related works, modify the abstract and introduction as needed, and 
expand on the methodology section by adding more details of the models and 
initial experimental results.  

*Length: 4 pages; similar to a conference short paper.*

## Model Requirements

Everyone will be required to implement baseline models and a more complex 
neural network model (i.e., not a Feedforward NN). For the baseline models, 
you may choose from any of the models discussed in class, but the most 
relevant model for the task based on your literature review is preferred. 
For the neural network model, you should choose whichever architecture is 
best suited for your task. For example, tasks using language-based features 
might choose RNNs or Transformer-based NNs, while tasks using images might 
choose Convolutional Neural Networks (CNNs). For evaluation, results should 
be reported for all models using at least the four basic metrics: precision, 
recall, accuracy, and F1 score. All code for the project must be submitted 
through D2L or GitHub.

## From Our Proposal

### Baseline model

**Logistic Regression Model**

Use a vocabulary of hateful/non-hateful words and assess how often they 
appear in sentences

### Complex Model

**Transformer - BERT**

## Metrics

This [article](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall)
gives an overview of each metric.

The metrics are defined in terms of the elements of the *confusion matrix*, 
which are as follows:

- $TP$ (**true positives**): The $+$ samples (correctly) predicted to be $+$
- $TN$ (**true negatives**): The $-$ samples (correctly) predicted to be $-$
- $FP$ (**false positives**): The $-$ samples (incorrectly) predicted to be $+$
- $FN$ (**false negatives**): The $+$ samples (incorrectly) predicted to be $-$

### Precision

The proportion of positive classifications that are actually positive.

$$
\text{Prevision}
=\frac{\text{correctly classified actual positives}}{\text{all classified as 
positives}}
=\frac{TP}{TP+FP}
$$

### Recall

The proportion of actual positives that are classified correctly as 
positives. Also called the *true positive rate (TPR)* or *probability of 
detection*

$$
\text{Recall}
=\frac{\text{correctly classified actual positives}}{\text{all 
actual positives}}
=\frac{TP}{TP+FN}
$$

### Accuracy

The proportion of all classifications that are correct.

$$
\text{Accuracy}
=\frac{\text{correct classifications}}{\text{all classifications}}
=\frac{TP+TN}{TP+TN+FP+FN}
$$

### F1 Score

A harmonic mean of *precision* & *recall*. 

$$
\text{F}1
=2\times\frac{\text{precision}\times\text{recall}}{\text{precision}+\text
{recall}}
=\frac{2TP}{2TP+FP+FN}
$$
