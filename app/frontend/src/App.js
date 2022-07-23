import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

// TODO move this into it's own file
function FormInput({movieRating, handleChange}) {
  return <div className="form-row row">
    <div className="col">
      <input name="movie"
        type="text"
        id={movieRating.movie}
        value={movieRating.movie}
        readOnly
      />
    </div>
    <div className="col">
      <form>
        <input name="rating"
          id={movieRating.movie}
          value={movieRating.rating}
          type="number"
          placeholder={movieRating.rating}
          min="0"
          max="100"
          onChange={handleChange}
        />
      </form>
    </div>
    <div className="col">
      <form>
        <select name="haveSeen"
          id={movieRating.movie}
          value={movieRating.haveSeen}
          onChange={handleChange}>
          <option value="True">I have seen this</option>
          <option value="False">I haven't seen this</option>
        </select>
      </form>
    </div>
  </div>
}

function App() {
  const [movies, setMovies] = useState([])

  // Dictionary of js objects that look like this: {movie: {movie}, rating: 0.0, haveSeen: "False" }
  const [movieRatings, setMovieRatings] = useState({});
  const handleChange = (evnt) => {
    var movie = evnt.target.id
    var changedProp = evnt.target.name
    var newValue = changedProp == "rating" ? parseInt(evnt.target.value) : evnt.target.value

    // Copy over existing data for the updated movie and set the changed property
    var newMovieData = {movie: movie, rating: movieRatings[movie].rating, haveSeen: movieRatings[movie].haveSeen}
    newMovieData[changedProp] = newValue
    
    // Javascript magic to update the state and render the page
    const newInput = (data) => ({ ...data, [movie]: newMovieData })
    setMovieRatings(newInput)
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

  return (
    <React.Fragment>
      <div className="App">
        <header className="App-header">
          <h1>Movie Reviewer Matcher</h1>
        </header>
        <p>Please enter your rating for each movie as a score from 0 to 100.</p>
        <div className="container">
          {movies.map(movie => (
            movieRatings[movie] = movie in movieRatings ? movieRatings[movie] : {movie: movie, rating: 0.0, haveSeen: "False"},
            <div className="row" key={movie}>
              <div className="col-sm-8">
                <FormInput movieRating={movieRatings[movie]}
                           handleChange={handleChange}
                />
              </div>
            </div>
          ))}
        </div>
      </div>
    </React.Fragment>
  );
}

export default App;
