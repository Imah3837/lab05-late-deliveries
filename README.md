# Late Deliveries Prediction

## Objective

Predict whether a food delivery order will arrive late.

## Dataset

Synthetic dataset generated using data.py.

## Features Used

### Numeric Features

- distance_km
- items
- hour
- courier_months

### Categorical Features

- weather
- day_type
- vehicle

## Excluded Features

- order_id
- prep_minutes
- customer_rating

## Train Test Split

- 75% Training
- 25% Testing
- Random State = 42
- Stratified Split

## Preprocessing

- Median Imputation
- Standard Scaling
- One Hot Encoding

## Models Compared

| Model | Accuracy |
|---------|---------|
| Dummy Classifier | 0.8440 |
| Logistic Regression | 0.8667 |
| Balanced Logistic Regression | 0.7373 |
| Random Forest | 0.8573 |

## Best Model

Logistic Regression

Reason:
Highest test accuracy among all evaluated models.

## Final Accuracy

0.8667