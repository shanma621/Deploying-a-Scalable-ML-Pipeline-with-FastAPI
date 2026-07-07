
import numpy as np
from sklearn.ensemble import RandomForestClassifier

from ml.data import apply_label
from ml.model import compute_model_metrics, train_model


# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_apply_labels():
    """
    Test that apply_label returns the expected string labels.
    """
    assert apply_label([1]) == ">50K"
    assert apply_label([0]) == "<=50K"


# TODO: implement the second test. Change the function name and input as needed
def test_train_model():
    """
    Test that train_model returns a RandomForestClassifier.
    """
    X_train = np.array([[0, 1], [1, 0], [1, 1], [0, 0]])
    y_train = np.array([0, 1, 1, 0])

    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Test that compute_model_metrics returns valid metric values.
    """
    y = np.array([1, 0, 1, 1])
    preds = np.array([1, 0, 0, 1])

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(fbeta, float)
