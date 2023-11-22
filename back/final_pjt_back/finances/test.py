import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

dic = {}
num = 1
user_data = pd.read_csv('./test.csv')
# print(user_data.head(5))
df = user_data[['id','age','salary', 'money','gender','address']]
print(df.head(5)) 
count_vector = CountVectorizer(ngram_range=(1,3))
c_vector_adress = count_vector.fit_transform(df['address'])

for i in range(len(df['address'])):
    if not df['address'][i] in dic:
        dic[df['address'][i]] = num
        num += 1
    df['address'][i] = dic[df['address'][i]]
normalization_df = (df - df.min())/(df.max() - df.min())
item_sim = cosine_similarity(normalization_df, normalization_df)
item_sim_df = pd.DataFrame(item_sim, index=normalization_df.id, columns=normalization_df.id)
print(item_sim_df.iloc[:4,:4])
