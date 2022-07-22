import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

function FormInput({movie, movieRating, handleChange }) {
  console.log(movieRating)
  return <div className="form-row row">
    <div className="col">
      <input name="movie"
        type="text"
        value={movie}
        readOnly
      />
    </div>
    <div className="col">
      <form>
        <input name="rating"
          value={movieRating.rating}
          type="number"
          placeholder="0"
          min="0"
          max="100"
          onChange={handleChange}
        />
      </form>
    </div>
    <div className="col">
      <form>
        <select name="haveSeen"
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
  const [movieRating, setMovieRating] = useState({ movie: "", rating: 0.0, haveSeen: "False" });

  const handleChange = (evnt) => {
    const newInput = (data) => ({ ...data, [evnt.target.name]: evnt.target.value })
    setMovieRating(newInput)
  }

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
            movieRating.movie = movie,
            <div className="row" key={movie}>
              <div className="col-sm-8">
                <FormInput key={movie} movie={movie}
                  movieRating={movieRating}
                  handleChange={handleChange} />
              </div>
            </div>
          ))}
        </div>
      </div>
    </React.Fragment>
  );

  // return (
  //   <div className="App">
  //     <header className="App-header">
  //       <h1>Movie Reviewer Matcher</h1>
  //       </header>
  //       <p>Please enter your rating for each movie as a score from 0 to 100.</p>
  //       <table width="100%">
  //         <thead>
  //           <tr>
  //             <th>Movie</th>
  //             <th>Rating</th>
  //             <th>Seen it?</th>
  //           </tr>
  //         </thead>
  //         <tbody>
  //           {movies.map(movie => (
  //             <tr>
  //               <td> {movie} </td>
  //               <td>
  //                   <input 
  //                     // value={this.state.value}
  //                     type="number" 
  //                     placeholder="0"
  //                     min="0" 
  //                     max="100"
  //                   />
  //               </td>
  //               <td>
  //                 <select>
  //                   <option value="true">I have seen this</option>
  //                   <option value="false">I haven't seen this</option>
  //                 </select>
  //               </td>
  //             </tr>
  //           ))}
  //         </tbody>
  //       </table>
  //       <form>
  //         <input type="submit" value="Submit" />
  //       </form>
  //   </div>
  // );
}

export default App;
