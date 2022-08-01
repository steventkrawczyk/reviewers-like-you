import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

import FormInput from './FormInput.js';

// Creates an individual row of form input to rate movies.
function createRow(movie, movieRatings, handleChange) {
  movieRatings[movie] = movie in movieRatings ? movieRatings[movie] : { movie: movie, rating: 0.0, haveSeen: "True" }
  return <div className="row" key={movie}>
    <div className="col-sm-8">
      <FormInput movieRating={movieRatings[movie]}
        handleChange={handleChange}
      />
    </div>
  </div>
}

// Displays movies to rate, and accepts form input.
function renderMoviePage(movies, movieRatings, handleChange, handleSubmit) {
  return <React.Fragment>
    <div className="App">
      <header className="App-header">
        <h1>Movie Reviewer Matcher</h1>
      </header>
      <p>Please enter your rating for each movie as a score from 0 to 100.</p>
      <div className="container">
        {movies.map(movie => createRow(movie, movieRatings, handleChange))}
        <input type="submit" value="Submit" onClick={handleSubmit} />
      </div>
    </div>
  </React.Fragment>
}

// Displays the author match, and creates a table of recommendations.
function renderMatchPage(author, recommendations) {
  return <React.Fragment>
    <div className="App">
      <header className="App-header">
        <h1>Movie Reviewer Matcher</h1>
      </header>
      <p>You have matched with reviewer: {author}. Check out their reviews below!</p>
      <div className="container">
        {recommendations.map(recommendation => (
          <div className="row" key={recommendation.movie}>
            <div className="col">
              Movie: {recommendation.movie}
            </div>
            <div className="col">
              Rating: {recommendation.rating * 100}
            </div>
          </div>
        ))}
      </div>
    </div>
  </React.Fragment>
}

function App() {
  const [movies, setMovies] = useState([])
  const [author, setAuthor] = useState("")
  const [recommendations, setRecommendations] = useState([])

  // Dictionary of js objects that look like this: {movie: {movie}, rating: 0.0, haveSeen: "False" }
  const [movieRatings, setMovieRatings] = useState({});
  const handleChange = (evnt) => {
    var movie = evnt.target.id
    var changedProp = evnt.target.name
    var newValue = changedProp === "rating" ? parseInt(evnt.target.value) : evnt.target.value

    // Copy over existing data for the updated movie and set the changed property
    var newMovieData = { movie: movie, rating: movieRatings[movie].rating, haveSeen: movieRatings[movie].haveSeen }
    newMovieData[changedProp] = newValue

    // Javascript magic to update the state and render the page
    const newInput = (data) => ({ ...data, [movie]: newMovieData })
    setMovieRatings(newInput)
  }

  const handleSubmit = (evnt) => {
    var userMovieRatings = {}
    Object.keys(movieRatings).forEach(function(movie) {
      if (movieRatings[movie].haveSeen === "True") {
        userMovieRatings[movie] = movieRatings[movie].rating.toFixed(3) / 100.0
      } else {
        // We use -1 to indicate that a movie has not been seen. This way, it can be handled by the backend.
        // For more info, see "Filtering by haveSeen":
        // https://docs.google.com/document/d/1E5aaVy49jOZzIXVVt2vu35q79hYqHlMsu5b1GxcZmDM/edit?usp=sharing
        userMovieRatings[movie] = -1
      }
    });

    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      data: JSON.stringify(userMovieRatings)
    };

    var requestUrl = 'http://127.0.0.1:5000/match'
    axios.post(requestUrl, requestOptions).then(response => {
      console.log("SUCCESS", response)
      var responseData = response.data.data

      // Set the recommendation and author data. We set recommendations first, so when we set author
      // the page can be fully rendered.
      setRecommendations(responseData.reviews)
      setAuthor(responseData.author)
    }).catch(error => {
      console.log(error)
    })

  }

  // First server call to get movies for rating
  useEffect(() => {
    axios.get('http://127.0.0.1:5000/movies').then(response => {
      console.log("SUCCESS", response)
      setMovies(response.data.data)
    }).catch(error => {
      console.log(error)
    })
  }, [])

  // Render the movie or match page, depending on if we've set the author data.
  return (author === "" ?
    renderMoviePage(movies, movieRatings, handleChange, handleSubmit) :
    renderMatchPage(author, recommendations));
}

export default App;
