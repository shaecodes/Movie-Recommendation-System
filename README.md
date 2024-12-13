# Movie-Recommendation-System

## Overview

This project features a **Movie Recommendation System** built using a dataset of over **8000 movie listings**. Each movie listing includes various information such as:

- Index
- Budget
- Genres
- Homepage
- ID
- Keywords
- Original Language
- Original Title
- Overview
- Popularity
- Production Companies
- Production Countries
- Release Date
- Revenue
- Runtime
- Spoken Languages
- Status
- Tagline
- Title
- Vote Average
- Vote Count
- Cast
- Crew
- Director

## Features

The movie recommendation system uses the following key features to generate recommendations:

- **Genres**
- **Keywords**
- **Tagline**
- **Cast**
- **Director**

These features are used to find similarities between movies and suggest movies that are most likely to match a user's preferences.

## TfidfVectorizer

The **TfidfVectorizer** is a feature extraction technique that transforms text data into numerical vectors. It works by converting words in the text into numbers based on their frequency, while considering how often those words appear across the entire dataset. This helps the model identify important words or phrases in a movie's description, which is essential for determining similarities between movies. The higher the weight of a word, the more important it is in determining similarity.

## Similarity Score

The similarity between movies is calculated using the **Cosine Similarity** metric. It measures the cosine of the angle between two non-zero vectors in the feature space. The similarity score ranges from **0** (no similarity) to **1** (perfect similarity). Higher similarity scores indicate that two movies are more alike, based on their genres, keywords, tagline, cast, and director.

## Streamlit

The movie recommendation system is built with **Streamlit**, a Python framework that allows for the creation of interactive web applications with minimal code. Streamlit makes it easy to visualize data and deploy machine learning models for users to interact with. In this project, Streamlit is used to create an intuitive interface where users can input movie preferences and receive personalized recommendations.
