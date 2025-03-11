"""
Defines the metrics used to test the performance of each model
"""

import numpy as np


def precision(y_hat: np.ndarray, y: np.ndarray) -> float:
    """
    The proportion of positively classified samples that are actually positive

    Mathematically: *TP* / (*TP* + *FP*)

    :param y_hat: An array of size *N* of the predicted classifications
    :param y: An array of size *N* of the actual classifications
    :return: The number of accurately classified positive samples divided by
        the number of samples classified as positive
    """
    ...

def recall(y_hat: np.ndarray, y: np.ndarray) -> float:
    """
    The proportion of positive samples that are correctly classified as
    positive

    Mathematically: *TP* / (*TP* + *FN*)

    :param y_hat: An array of size *N* of the predicted classifications
    :param y: An array of size *N* of the actual classifications
    :return: The number of accurately classified positive samples divided by
        the number of positive samples
    """
    ...

def accuracy(y_hat: np.ndarray, y: np.ndarray) -> float:
    """
    The proportion of all classifications that are correct

    Mathematically: (*TP* + *TN*) / (*TP* + *TN* + *FP* + *FN*)

    :param y_hat: An array of size *N* of the predicted classifications
    :param y: An array of size *N* of the actual classifications
    :return: The number of accurately classified samples divided by the
        number of samples
    """
    ...

def F1(y_hat: np.ndarray, y: np.ndarray) -> float:
    """
    A harmonic mean of ``precision`` and ``recall``

    Mathematically: *2TP* / (*2TP* + *FP* + *FN*)

    :param y_hat: An array of size *N* of the predicted classifications
    :param y: An array of size *N* of the actual classifications
    :return: The F1 score (the harmonic mean of the precision and the recall)
    """
    ...