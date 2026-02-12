import numpy as np


# Calculate the dice coefficient
def dice(gt: np.ndarray, pred: np.ndarray) -> float:
    assert gt.shape == pred.shape

    intersection = np.logical_and(gt, pred).sum()
    gt_fg = gt.sum()
    pred_fg = pred.sum()

    if gt_fg + pred_fg == 0:
        return 1.0

    return 2.0 * intersection / (gt_fg + pred_fg)


# Calculate the intersection over union
def iou(gt: np.ndarray, pred: np.ndarray) -> float:
    assert gt.shape == pred.shape

    intersection = np.logical_and(gt, pred).sum()
    union = np.logical_or(gt, pred).sum()

    if union == 0:
        return 1.0

    return intersection / union
