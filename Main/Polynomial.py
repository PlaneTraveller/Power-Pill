import numpy
import pandas
import matplotlib.pyplot as pyplot
import sklearn.pipeline as pipeline
import sklearn.linear_model as linear_model
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

model = pipeline.make_pipeline(PolynomialFeatures(28),
                               linear_model.LinearRegression())
with open('./Main/oldOut/California.csv') as csv:
    input = pandas.read_csv(csv)
input['number'] = input.index.values
date = input.iloc[260:320, 3].values
date = date[:, numpy.newaxis]
case = input.iloc[260:320, 1].values
date_train, date_test, case_train, case_test = train_test_split(date,
                                                                case,
                                                                test_size=0.3)
model.fit(date_train, case_train)
print(type(case_train))

MSE = mean_squared_error(case_train, model.predict(date_train))
px = numpy.linspace(date_train.min(), date_train.max(), 1000)
px = px.reshape(-1, 1)
pred_py = model.predict(px)
pyplot.scatter(date_train, case_train, s=60)
pyplot.plot(px, pred_py)
pyplot.tight_layout()
pyplot.show()
