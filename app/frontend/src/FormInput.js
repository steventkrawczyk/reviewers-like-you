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

export default FormInput;