# Movie Recommender System
A content based movie recommender system using cosine similarity
This project is a Movie Recommender System built using Streamlit and FastAPI. It provides personalized movie recommendations based on user preferences. To use the system, follow the instructions below.

## Images
<img width="1496" alt="Screenshot 2023-10-22 at 10 55 17 PM" src="https://github.com/ameyagidh/MovieRecommendationSystem/assets/65457905/58bb0a7a-b8ad-4629-96f8-744766cf8138">
<img width="1496" alt="Screenshot 2023-10-22 at 10 55 36 PM" src="https://github.com/ameyagidh/MovieRecommendationSystem/assets/65457905/5baaedcf-ae7b-4cf1-b70e-16fd26c7ab6c">
<img width="1496" alt="Screenshot 2023-10-22 at 10 55 43 PM" src="https://github.com/ameyagidh/MovieRecommendationSystem/assets/65457905/9ceae3e1-1e06-4bcf-96a3-d6671fd14929">
<img width="1496" alt="Screenshot 2023-10-22 at 10 56 29 PM" src="https://github.com/ameyagidh/MovieRecommendationSystem/assets/65457905/bdbbefdf-3139-4985-acaf-f18120e5acfb">


## Instructions

### Step 1: Setup the Environment

1. Clone this GitHub repository to your local machine:

   ```bash
   git clone https://github.com/ameyagidh/MovieRecommendationSystem.git
   ```

2. Change to the project directory:

   ```bash
   cd movie-recommender
   ```

3. Make sure you have the required dependencies installed. You can do this using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

### Step 2: Download Movie Data

1. Download the dataset containing movie information and credits from TMDb 5000 Movies Dataset. You can find the dataset [here](https://www.kaggle.com/tmdb/tmdb-movie-metadata). Place the downloaded CSV files in the `data` directory.

### Step 3: Run the Application

1. Start the FastAPI server. Open a terminal and run:

   ```bash
   uvicorn app:app --reload
   ```

   This will start the FastAPI server, which provides the recommendation API.

2. Open another terminal, navigate to the project directory, and run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

3. Open your web browser and go to the provided URL (usually http://localhost:8501). You should see the Movie Recommender System web application.

### Step 4: Use the Movie Recommender

1. In the web application, you can search for movies by title, genre, or actor's name.

2. Rate the movies you've watched, and the system will provide personalized recommendations based on your preferences.

3. Explore recommended movies, get movie details, and enjoy personalized movie suggestions.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and create a pull request with your changes.

## License

This project is licensed under the [Your License Name] License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or need assistance, please contact Ameya Santosh Gidh at ameyagidh2@gmail.com.
