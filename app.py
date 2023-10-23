import pickle
import streamlit as st
import requests


# Function to fetch movie poster
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # Fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


# Streamlit layout and design improvements
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon=":movie_camera:",
    layout="wide",
)

st.title('Movie Recommender System')

# Sidebar for user customization
st.sidebar.title("Customization")

# Allow users to choose themes
theme = st.sidebar.selectbox("Select Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown('<style>body {background-color: #181818; color: white;}</style>', unsafe_allow_html=True)

# User input and recommendation
st.subheader("Choose a Movie")
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # Improved layout with responsive design
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]

    for i, col in enumerate(columns):
        with col:
            st.image(recommended_movie_posters[i], use_column_width=True)
            st.write(recommended_movie_names[i])
