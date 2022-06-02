import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


df = pd.read_csv("archive/testset.csv")
# print(df._rain)
print(df["datetime_utc"])
print(df.datetime_utc)
print(df[" _rain"])
print(df._rain)

# X = df.iloc[:, [3, 4, 9, 10, 12, 13]]
# y = df.loc[:, " _rain"]


# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )
# clf = tree.DecisionTreeClassifier(max_leaf_nodes=3)
# clf = clf.fit(X_train, y_train)

# y_preds = clf.predict(X_test)

# print(
#     f"Accuracy in India weather datset: {accuracy_score(y_pred=y_preds, y_true=y_test)}"
# )

# ## Doing analysis in seattle dataset

# weather_df = pd.read_csv("seattle-weather.csv")
# weather_df[["year", "month", "day"]] = weather_df["date"].str.split("-", expand=True)

# weather_df = weather_df.drop(columns=["date"])
# # print(weather_df.head())

# y = weather_df["weather"]
# X = weather_df.drop(columns=["weather"], axis=1)

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# clf = tree.DecisionTreeClassifier(random_state=0, max_depth=5)
# clf.fit(X_train, y_train)

# y_preds = clf.predict(X_test)

# print(
#     f"Accuracy in Seattle Dataset - 1: {accuracy_score(y_pred=y_preds, y_true=y_test)}"
# )
