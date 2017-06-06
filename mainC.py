import webapp2



















class Index(webapp2.RequestHandler):


def getCurrentListOfMovies():
    return ["Moonlight", "Twelve Years a Slave", "Begin Again", "Sing Street"]

def get(self):

    edit_header = "<h3>Edit My Watchlist</h3>"

    movieOptions = ''
    for movie in getCurrentListOfMovies():
        movieOptions += '<option value="{0}">{0}</option>'.format(movie)
        # option value
        add_form = """
        <form action="/add" method="post">
            <label>
                I want to add_form
                <input type="text" name="new-movie"/>
                to my watchlist



        crossoff_form = """
        <form action="/cross-off" method="post">
            <label>
                I want to cross off
                <select name="crossed-off-movie">
                    {0}
                <option value="NotOnList">NotOnList</option
                </select>

        def post(self):
            crossed_off_movie = self.request.get("crossed-off-movie")

            if crossed_off_movie not in getCurrentListOfMovies():

                self.redirect("/?error={0} is not in your list of movies".format(crossed_off_movie))

            crossed_off_movie_element = "<strike>" + crossed_off_movie + "</strike>" + crossed_off_movie + "<strike>"
