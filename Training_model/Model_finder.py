from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression


class Best_model_finder:
    def __init__(self, X_train, X_test, Y_train, y_test):
        self.X_train = X_train
        self.X_test = X_test
        self.Y_train = Y_train
        self.y_test = y_test

    def linearregression(self):
        linear_model = LinearRegression()
        linear_model.fit(self.X_train, self.Y_train)
        Y_predicted = linear_model.predict(self.X_test)
        return r2_score(self.y_test, Y_predicted),linear_model

    def random_forest_regression(self):
        RFR_model = RandomForestRegressor(n_estimators=500, random_state=329, min_samples_leaf=.0001)
        RFR_model.fit(self.X_train, self.Y_train)
        y_predict = RFR_model.predict(self.X_test)
        return r2_score(self.y_test, y_predict), RFR_model

    def decision_tree_regression(self):
        DTree = DecisionTreeRegressor(min_samples_leaf=.0001)
        DTree.fit(self.X_train, self.Y_train)
        y_predict = DTree.predict(self.X_test)
        return r2_score(self.y_test, y_predict), DTree

    def extra_tree_regression(self):
        ETR_model = ExtraTreesRegressor(n_estimators=100)
        ETR_model.fit(self.X_train, self.Y_train)
        y_predict = ETR_model.predict(self.X_test)
        return r2_score(self.y_test, y_predict), ETR_model

    def comapre_all_model(self):
        model_with_score = {self.linearregression(): self.linearregression()[0],
                            self.random_forest_regression(): self.random_forest_regression()[0],
                            self.decision_tree_regression(): self.decision_tree_regression()[0],
                            self.extra_tree_regression(): self.extra_tree_regression()[0]}
        Max_accurate_model_score = max(list(model_with_score.values()))
        model_name = [key for key, values in model_with_score.items() if values == Max_accurate_model_score][0]
        return model_name
