#ifndef MOVIE_H
#define MOVIE_H

class Customer;
#include <iostream>
#include "customer.h"


const int LIST_SIZE = 20;

using namespace std;
class Movie
{
public:
    Movie();
    Movie(string gName);
    void setName(string name);
    string getName();
    void setID(string id);
    string getID();
    void addCustomer(Customer *other);
    void deleteCustomer(int index);
    Customer* getCustomer(int index);
    void print();
    int getIndex();

private:
    string name;
    string id;
    Customer** customers;
    int currentIndex;
};

#endif // MOVIE_H
