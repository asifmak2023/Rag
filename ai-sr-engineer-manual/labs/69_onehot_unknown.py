import pandas as pd
from sklearn.preprocessing import OneHotEncoder

train = pd.DataFrame({"city": ["KHI", "LHE", "KHI"]})
test = pd.DataFrame({"city": ["KHI", "ISB"]})
enc = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
enc.fit(train)
print("train", enc.transform(train))
print("test", enc.transform(test))
print("names", enc.get_feature_names_out())
assert enc.transform(test).shape[1] == enc.transform(train).shape[1]
