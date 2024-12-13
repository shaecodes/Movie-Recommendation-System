import streamlit as st
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movie_data = pd.read_csv('movies.csv')

selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
for feature in selected_features:
    movie_data[feature] = movie_data[feature].fillna('')

movie_data['combined_features'] = movie_data['genres'] + ' ' + movie_data['keywords'] + ' ' + movie_data['tagline'] + ' ' + movie_data['cast'] + ' ' + movie_data['director']

vectorizer = TfidfVectorizer(stop_words='english')
feature_vectors = vectorizer.fit_transform(movie_data['combined_features'])

similarity = cosine_similarity(feature_vectors)

def recommend_movie(movie_title, movie_data, similarity):
    try:
        idx = movie_data[movie_data['title'] == movie_title].index[0]
    except IndexError:
        st.write("Movie title not found in the dataset.")
        return None

    similarity_scores = list(enumerate(similarity[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similar_movies = similarity_scores[1:6]

    movie_indices = [i[0] for i in similar_movies]
    return movie_data['title'].iloc[movie_indices]

st.title('Movie Recommendation System')
st.write('Enter a movie title to get recommendations based on similar genres, keywords, and other features.')

movie_name = st.text_input('Enter your favorite movie name:', '')

if movie_name:
    recommendations = recommend_movie(movie_name, movie_data, similarity)
    if recommendations is not None:
        st.write(f"**Top 5 recommendations based on {movie_name}:**")
        for idx, movie in enumerate(recommendations, 1):
            st.write(f"{idx}. {movie}")
