#include "customer.h"

Customer::Customer()
{

}

Customer::Customer(string gName, int number){
    name = gName;
    phoneNumber = number;
    movies = new Movie*[LIST_SIZE];
    currentIndex = 0;
}

string Customer::getName(){
    return name;
}

void Customer::setName(string sName){
    name = sName;
}

int Customer::getID(){
    return id;
}

void Customer::setID(int sID){
    id = sID;
}

int Customer::getNumber(){
    return phoneNumber;
}

void Customer::setNumber(int number){
    phoneNumber = number;
}

void Customer::addMovie(Movie* newMovie){
    movies[currentIndex] = newMovie;
    currentIndex++;
}
Movie* Customer::getMovieAtIndex(int index){
    return movies[index];
}

void Customer::print(){
    cout << name << " " << phoneNumber << endl;
}

void Customer::printAll(){
    this->print();
    for (int i = 0; i < currentIndex; i++){
        cout << "---";
        movies[i]->print();
    }
    cout << endl;
}

void Customer::deleteMovie(string g){
    int movieIndex;
    for (int i = 0; i < currentIndex; i++){
        if(movies[i]->getName() == g){
            movieIndex = i;
            break;
        }
    }
    for (int i = movieIndex; i < currentIndex; i++){
        movies[i] = movies[i + 1];
    }
    currentIndex--;
    movies[currentIndex] = nullptr;
}
