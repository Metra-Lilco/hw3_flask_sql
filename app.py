import sqlite3

from flask import Flask

from tables_create import create_customers, create_tracks


app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route("/names/")
def get_unique_names():
    con = sqlite3.connect("flask_sql.db")
    cur = con.cursor()
    query_unique_names = '''
    SELECT COUNT(DISTINCT first_name) FROM customers
    '''
    cur.execute(query_unique_names)
    result = cur.fetchone()
    if result:
        con.close()
        return f"There is <b>{result[0]}</b> unique names in 'customers'"
    con.close()
    return "<b>There is no unique names in 'customers'</b>"

@app.route("/tracks/")
def get_tracks_count():
    con = sqlite3.connect("flask_sql.db")
    cur = con.cursor()
    query_tracks_count = '''
    SELECT COUNT (*) FROM tracks
    '''
    cur.execute(query_tracks_count)
    result = cur.fetchone()
    if result:
        con.close()
        return f"There is <b>{result[0]}</b> tracks in 'tracks' table"
    con.close()
    return "<b>The 'tracks' table is empty!</b>"

@app.route("/tracks-sec/")
def get_tracks_info():
    con = sqlite3.connect("flask_sql.db")
    cur = con.cursor()
    query_tracks_info = '''
    SELECT duration, ID, artist, song, release_date FROM tracks
    '''
    cur.execute(query_tracks_info)
    result = cur.fetchall()
    con.close()
    if result:
        track_rows = ""
        for track in result:
            duration, ID, artist, song, release_date = track
            track_row = f"<li style='color:navy'><b>Duration:</b> {duration} \
                        <b>sec.</b>, <b>Track ID:</b> {ID}, \
                        <b>Artist:</b> {artist}, <b>Song:</b> {song}, \
                        <b>Release date:</b> {release_date}</li>"
            track_rows += track_row
        return track_rows
    return "<b>The 'tracks' table is empty!</b>"

if __name__ == "__main__":
    create_customers()
    create_tracks()
    app.run()
