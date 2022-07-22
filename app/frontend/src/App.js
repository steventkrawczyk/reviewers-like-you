import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

function App() {
  const [movies, setMovies] = useState([])

  useEffect(()=>{
    axios.get('http://127.0.0.1:5000/movies').then(response => {
      console.log("SUCCESS", response)
      setMovies(response.data.data)
    }).catch(error => {
      console.log(error)
    })
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <h1>Movie Reviewer Matcher</h1>
        </header>
        <p>Please enter your rating for each movie as a score from 0 to 100.</p>
        <table width="100%">
          <thead>
            <tr>
              <th>Movie</th>
              <th>Rating</th>
              <th>Seen it?</th>
            </tr>
          </thead>
          <tbody>
            {movies.map(movie => (
              <tr>
                <td> {movie} </td>
                <td>
                  <form>
                    <input type="text" placeholder="Rating"/>
                  </form>
                </td>
                <td>
                  <select>
                    <option value="true">I have seen this</option>
                    <option value="false">I haven't seen this</option>
                  </select>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        <form>
          <input type="submit" value="Submit" />
        </form>
    </div>
  );
}

export default App;
