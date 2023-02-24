import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import csv


def create_test_data_file(loan_amount, salary):
    loan_amount_000s = loan_amount
    applicant_income_000s = salary
    with open('test_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['loan_amount_000s', 'applicant_income_000s'])
        writer.writerow([loan_amount_000s, applicant_income_000s])


def pred_model(loan_amount, salary):
    create_test_data_file(loan_amount, salary)
    # load data
    ct_data = pd.read_csv("./ct_2017_Cont_output_no_outliers.csv")
    # create variables
    data_cols = ['loan_amount_000s', "applicant_income_000s"]
    X = ct_data[data_cols]
    Y = ct_data["action_taken"]
    # train model
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=16)
    logreg = LogisticRegression(random_state=16)
    logreg.fit(X_train, y_train)
    # load test
    test = pd.read_csv('./test_data.csv')
    # return true is approved
    return logreg.predict(test)[0] == 1
