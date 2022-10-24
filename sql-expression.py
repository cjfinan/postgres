from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# making the connection
with db.connect() as connection:

    # query 1 select all records from the artist table
    # select_query = artist_table.select()

    # query 2 select on the name colum from the artist table
    # select_query = artist_table.select().with_only_columns(
    # [artist_table.c.Name])

    # query 3 select only queen from the artist table
    # select_query = artist_table.select().where(
    # artist_table.c.Name == "Queen")

    # query 4 select only by artist Id #51 from the artist table
    select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    results = connection.execute(select_query)
    for result in results:
        print(result)
