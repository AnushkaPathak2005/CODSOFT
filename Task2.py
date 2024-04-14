Import pandas as pd

Import numpy as np

Sample user-item preference data

data = {

'User': ['User1', 'User2', 'User3', 'User4', 'User'],

omg 2': [5, 4, 0, 0, 31,

'gader2': [4, 5, 4, 0, 2],

'bawaal': [0, 3, 6, 5, 0],

'coat': [2, 0, 5, 4, 0],

'rocky and rani': [0, 0, 4, 5, 4]

#Create a DataFrame from the data

df pd.DataFrame(data)

# Calculate the similarity matrix using cosine similarity

similarity_matrix = np.dot(df.iloc[:, 1:].fillna(0), df.iloc[:, 1:].fillna(8).T) /(

np.linalg.norm(df.iloc[:, 1:].fillna(0), axis-1) [:, None] *

np.linalg.norm(df.iloc[:, 1:].fillna(@).T, axis-6)

Convert the similarity matrix into a DataFrame

)

similarity_df pd.DataFrame (similarity_matrix, index-df['User'], columns=df['User'])
Function to recommend movies to a user

def recommend_movies(user, num_recommendations-3):

user_preferences df [df['User user].iloc[:, 1:] similar_users similarity_df[user].sort_values(ascending False).index [1:] #Exclude the user itself

recommendations = []

for similar user in similar_users: rimilan user preferences dflafl'User 
similar_user in similar_users:

similar_user_preferences df [df['User'] - similar_user].iloc[:, 1:]

new_recommendations (similar_user_preferences - user_preferences).sum(axis-1) recommendations.extend(new_recommendations[new_recommendations > 0].index.tolist())

if len(recommendations) > num_recommendations:

break

return df.columns [1:] [recommendations]

Test the recommendation system user_to_recommend = 'User1'

I recommended_movies recommend_movies(user_to_recommend)

 print(f"Recommended movies for (user_to_recommend): (recommended_movies}")
