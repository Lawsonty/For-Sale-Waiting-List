#include "movielist.h"

MovieList::MovieList()
{
    currentIndex = 0;
    maxMovies = 100;
    movies = new Movie[maxMovies];
}

void MovieList::addMovie(string mName){
    movies[currentIndex] = Movie(mName);
    currentIndex++;
}

void MovieList::deleteMovie(){
//todo

}

void MovieList::print(){
    for (int i = 0; i < currentIndex; i++){
    cout << movies[i].getName() << endl;
        for (int j = 0; j < movies[i].getIndex(); j++){
           cout << j + 1 << ") ";
           movies[i].getCustomer(j)->print();
        }
    }
}

Movie* MovieList::getMoviebyIndex(int n){
    return &movies[n];
}

int MovieList::getCurrentIndex(){
    return currentIndex;
}
