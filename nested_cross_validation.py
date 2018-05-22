from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score


if __name__ == '__main__':
    digits = load_digits()  # (1797, 64)

    pipe = make_pipeline(StandardScaler(), SVC())
    param_grid = {'svc__C':     [0.1, 0.3, 1, 3, 10],
                  'svc__gamma': [0.1, 0.3, 1, 3, 10]}

    grid = GridSearchCV(pipe, param_grid=param_grid, cv=5, n_jobs=-1)


    # Ordinary（Get Generalized Model）
    X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, random_state=0)

    grid.fit(X_train, y_train)

    print('Best Parameters: {}'.format(grid.best_params_))
    print('Best CV Score: {:.3f}'.format(grid.best_score_))
    print('Test Set Accuracy: {:.3f}'.format(grid.score(X_test, y_test)))
    # Best Parameters: {'svc__C': 3, 'svc__gamma': 0.1}
    # Best CV Score: 0.933
    # Test Set Accuracy: 0.942


    # Nested CV（Show Potential Score）
    scores = cross_val_score(grid, digits.data, digits.target, cv=5)

    print('CV scores:', scores)
    print('Mean CV scores: {:.3f}'.format(scores.mean()))
    # CV scores: [0.93681319 0.85911602 0.8718663  0.89915966 0.88169014]
    # Mean CV scores: 0.890
