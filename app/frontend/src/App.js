import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

import FormInput from './FormInput.js';

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
    const searchParams = new URLSearchParams();
    movies.map(movie => {
      if (movieRatings[movie].haveSeen === "True") {
        searchParams.append(movie, movieRatings[movie].rating / 100)
      } else {
        // We use -1 to indicate that a movie has not been seen. This way, it can be handled by the backend.
        // For more info, see "Filtering by haveSeen":
        // https://docs.google.com/document/d/1E5aaVy49jOZzIXVVt2vu35q79hYqHlMsu5b1GxcZmDM/edit?usp=sharing
        searchParams.append(movie, -1)
      }
      return 0
    })
    var requestUrl = 'http://127.0.0.1:5000/match?' + searchParams.toString()

    axios.get(requestUrl).then(response => {
      console.log("SUCCESS", response)
      var responseData = response.data.data
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

  return (author === "" ?
    <React.Fragment>
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
    </React.Fragment> :
    <React.Fragment>
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
  );
}

export default App;
