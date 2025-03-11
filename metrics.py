import numpy as np


def precision(y_hat, y):
    tp = np.where(y_hat == 1 and y == 1, 1, 0)  # true positives (TP)
    cp = np.where(y_hat == 1, 1, 0)  # all classified as positives (TP + FP)

    # (TP) / (TP + FP)
    return np.sum(tp) / np.sum(cp)


def recall(y_hat, y):
    tp = np.where(y_hat == 1 and y == 1, 1, 0)  # true positives (TP)
    ap = np.where(y == 1, 1, 0)  # all actual positives (TP + FN)

    # (TP) / (TP + FN)
    return np.sum(tp) / np.sum(ap)


def accuracy(y_hat, y):
    cc = np.where(y_hat == y, 1, 0)  # correct classifications (TP + TN)

    # (TP + TN) / (TP + TN + FP + FN)
    return np.sum(cc) / y_hat.shape[0]  # all classifications


def F1(y_hat, y):
    tp = np.where(y_hat == 1 and y == 1, 1, 0)  # true positives (TP)

    ic = np.where(y_hat != y, 1, 0)  # incorrect classifications (FP + FN)

    # 2TP / (2TP + FP + FN)
    return (2 * np.sum(tp)) / (2 * np.sum(tp) + np.sum(ic))