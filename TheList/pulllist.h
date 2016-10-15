#ifndef PULLLIST_H
#define PULLLIST_H


#include "customerlist.h"
#include "movielist.h"

using namespace std;

class PullList
{
public:
    PullList(MovieList& mList, CustomerList& cList);
    void pull(MovieList& mList, CustomerList& cList);

private:
    CustomerList pullCust;
    MovieList pullMovies;
    string** toBePulled;

};

#endif // PULLLIST_H
