#ifndef MOVIELIST_H
#define MOVIELIST_H

#include "movie.h"
#include "customerlist.h"

class MovieList
{
public:
    MovieList();
    void addMovie(string mName);
    void deleteMovie();
    void print();
    Movie* getMoviebyIndex(int n);
    int getCurrentIndex();

private:
    Movie* movies;
    int maxMovies;
    int currentIndex;
};

#endif // MOVIELIST_H
