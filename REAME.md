# Time Series Repository
## About the Module

In this module, you will learn why, when, and how to employ forecasting methods for predicting temporal events, i.e. events that occur over time. You will learn how to evaluate and improve performance of the model. You will understand the differences in stats based, or parametric, and machine learning based, or non-parametric methods.

- We will acquire data via: a REST API, Cloud File Storage (AWS-S3), and SQL.
- We will practice using pandas to operate on dates and datetime values
- We will address some of the complexities of time series data, including seasonality, sampling, and storing.
- We will create forecasts, or time series models, using Simple Average, Moving Average, Holts Linear Trend, and Prophet, and Autoregressive model.
- We will practice forecasting sales (store/items sales data) and learn techniques for working with with time series data like logs (user behavior) or other financial measurements over time.


## Time series vocabulary

- **Temporal:** Relating to time.
- **Periodic:** Occurring at intervals.
- **Resampling in Time Series:** Changing the frequency of your data points.
- **Stationary Process:** Distribution does not change over time.
- **Trend:** Long term progression (increasing, decreasing, e.g.)
- **Seasonality:** Changes in patterns due to seasonal factors.
- **Heteroskedasticity:** Changes in variance over time.
- **Autocorrelation:** 'Regression of self', used to detect non-randomness in data. It is a correlation coefficient, but instead of between two different variables, it is between the values of the same variable at two different times.
- **Lag Variables:** Previous time steps.