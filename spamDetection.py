import pandas as pd
from sklearn import feature_extraction
from  sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def initialize():
    df = pd.read_csv('spam.csv', encoding='ISO-8859-1')

    df.drop(columns=['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace=True)
    df.rename(columns={'v1': 'Category', 'v2': 'Message'}, inplace=True)

    data = df.where((pd.notnull(df)), '')

    data.loc[data['Category'] == 'spam', 'Category'] = 0
    data.loc[data['Category'] == 'ham', 'Category'] = 1

    X = data['Message']
    Y = data['Category']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

    feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
    X_train_features = feature_extraction.fit_transform(X_train)

    Y_train = Y_train.astype('int')
    model = LogisticRegression()

    model.fit(X_train_features, Y_train)

    return model, feature_extraction
def spam_detector(message,model, feature_extraction):

    input_your_mail = [message]
    input_data_features = feature_extraction.transform(input_your_mail)
    prediction = model.predict(input_data_features)
    if prediction == 1:
        return False
    else:
        return True


