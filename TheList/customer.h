#ifndef CUSTOMER_H
#define CUSTOMER_H

class Movie;
#include <iostream>
#include "movie.h"

using namespace std;

class Customer
{
public:
    Customer();
    Customer(string gName, int number);
    string getName();
    void setName(string sName);
    int getID();
    void setID(int sID);
    int getNumber();
    void setNumber(int number);
    void addMovie(Movie* newMovie);
    Movie* getMovieAtIndex(int index);
    void print();
    void printAll();
    void deleteMovie(string g);


private:
    string name;
    int phoneNumber;
    int id;
    Movie** movies;
    int currentIndex;
};

#endif // CUSTOMER_H
