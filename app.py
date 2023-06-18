import pandas as pd
import streamlit as st
import pickle


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = [movies.iloc[i[0]].title for i in distances[1:6]]
    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Assuming you have a similarity matrix stored in a pickle file called 'similarity.pkl'
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.write('Recommended Movies:')
    for movie in recommendations:
        st.write(movie)
