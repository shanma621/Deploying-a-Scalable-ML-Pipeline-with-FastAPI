# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This project uses a Random Forest Classifier implemented with scikit-learn to predict whether an individual's annual income is greater than $50K based on U.S. Census data. Categorical features are one-hot encoded before training, and the trained model and encoder are saved as pickle files for later inference.

## Intended Use

This model is intended for educational purposes as part of the Udacity Machine Learning DevOps project. It demonstrates a complete machine learning pipeline including data preprocessing, model training, evaluation, serialization, and deployment using FastAPI. It should not be used to make real-world employment, financial, or other high-impact decisions.

## Training Data

The model was trained using the Census Income dataset provided with the project starter code. The dataset was randomly split into training and testing sets using an 80/20 train-test split with a fixed random state for reproducibility. Categorical features were one-hot encoded before model training.

## Evaluation Data

The evaluation data consists of the 20% holdout test set created from the original Census Income dataset. The same preprocessing pipeline used for the training data was applied to the test data using the fitted encoder.

## Metrics

The model was evaluated using precision, recall, and F1 score.

- Precision: 0.7419
- Recall: 0.6384
- F1 Score: 0.6863

## Ethical Considerations

The Census Income dataset contains demographic attributes such as race, sex, marital status, and native country. Models trained on these data may learn historical biases present in the dataset. Predictions from this model should not be used to make decisions that affect individuals in employment, lending, housing, or other areas where fairness is important.

## Caveats and Recommendations

This model was developed for demonstration and educational purposes only. Performance depends on the quality and representativeness of the training data. Future improvements could include hyperparameter tuning, additional model evaluation, fairness analysis, and monitoring for performance degradation on new data.