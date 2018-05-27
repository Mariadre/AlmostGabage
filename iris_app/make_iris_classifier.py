# For Train
# ------------------------------------------------------------
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.pipeline import make_pipeline
# from sklearn.svm import SVC
# from sklearn.preprocessing import StandardScaler
# from sklearn.externals import joblib
#
#
# iris = load_iris()
# X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)
#
# pipe = make_pipeline(StandardScaler(), SVC(C=3, gamma=0.1))
# pipe.fit(X_train, y_train)
#
# print(pipe.score(X_test, y_test))  # 97.4%
# joblib.dump(pipe, 'model.pkl')


# For Grid Search
# ------------------------------------------------------------
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split, GridSearchCV
# from sklearn.pipeline import make_pipeline
# from sklearn.svm import SVC
# from sklearn.preprocessing import StandardScaler
#
#
# iris = load_iris()
# X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)
#
# pipe = make_pipeline(StandardScaler(), SVC())
# param_grid = {'svc__C':     [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 100],
#               'svc__gamma': [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 100]}
#
# grid = GridSearchCV(pipe, param_grid=param_grid, cv=5)
# grid.fit(X_train, y_train)
#
#
# print('Best Parameters: {}'.format(grid.best_params_))
# print('Best CV Score: {:.3f}'.format(grid.best_score_))
# print('Best Test Score: {:.3f}'.format(grid.score(X_test, y_test)))
