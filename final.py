import streamlit as st
import pickle
import requests

# Load movie list and similarity matrix
movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Which movie would you like to recommend?',
    movies_list['title'].values
)

if st.button('Recommend'):
    # Get index of selected movie
    selected_movie_index = movies_list[movies_list['title'] == selected_movie_name].index[0]

    # Retrieve similarity scores for selected movie
    similarity_scores = list(enumerate(similarity[selected_movie_index]))

    # Sort movies based on similarity scores
    similar_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Display top 5 recommended movies
    recommended_movies = [movies_list.iloc[movie[0]]['title'] for movie in similar_movies[1:6]]
    st.write('Top 5 recommended movies:')
    for movie in recommended_movies:
        st.write(movie)
