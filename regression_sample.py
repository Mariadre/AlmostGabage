from sklearn.datasets import load_boston

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


SVR_C = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 100, 300]
SVR_GAMMA = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 100, 300]
SVR_DEGREE = [1, 2, 3]
RIDGE_ALPHA = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 100, 300]
LASSO_ALPHA = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 100, 300]
ELASTICNET_ALPHA = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 100, 300]
ELASTICNET_L1_RATIO = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 0.5, 0.8, 1]
CV = 5

boston = load_boston()
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, random_state=0)


def estimator_grid_search():
    pipe = Pipeline([('preprocessing', StandardScaler()), ('estimator', SVR())])

    param_grid = [
        {'estimator': [SVR()],
         'preprocessing': [None, StandardScaler()],
         'estimator__C': SVR_C,
         'estimator__gamma': SVR_GAMMA,
         'estimator__degree': SVR_DEGREE},
        {'estimator': [LinearRegression()],
         'preprocessing': [None, StandardScaler()]},
        {'estimator': [Ridge()],
         'preprocessing': [None, StandardScaler()],
         'estimator__alpha': RIDGE_ALPHA},
        {'estimator': [Lasso()],
         'preprocessing': [None, StandardScaler()],
         'estimator__alpha': LASSO_ALPHA},
        {'estimator': [ElasticNet()],
         'preprocessing': [None, StandardScaler()],
         'estimator__alpha': ELASTICNET_ALPHA,
         'estimator__l1_ratio': ELASTICNET_L1_RATIO},
    ]

    grid = GridSearchCV(pipe, param_grid=param_grid, cv=CV, n_jobs=-1)
    grid.fit(X_train, y_train)

    print('Best parameters:', grid.best_params_)
    print('Best cross-validation score: {:.3f}'.format(grid.best_score_))
    print('Test Accuracy: {:.3f}'.format(grid.score(X_test, y_test)))


if __name__ == '__main__':
    estimator_grid_search()
