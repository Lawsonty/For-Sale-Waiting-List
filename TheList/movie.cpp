#include "movie.h"
#include "customer.h"

Movie::Movie()
{

}
Movie::Movie(string gName){
    name = gName;
    customers = new Customer*[LIST_SIZE];
    currentIndex = 0;
}

void Movie::setName(string name){
    this->name = name;
}

string Movie::getName(){
    return name;
}

void Movie::setID(string id){
    this->id = id;
}

string Movie::getID(){
    return id;
}

void Movie::addCustomer(Customer* newCustomer){
    customers[currentIndex] = newCustomer;
    currentIndex++;
    newCustomer->addMovie(this);
}

void Movie::deleteCustomer(int index){
    customers[index]->deleteMovie(this->name);
    for (int i = index; i < currentIndex; i++){
        customers[i] = customers[i + 1];
    }
    currentIndex--;
    customers[currentIndex] = nullptr;
}

Customer* Movie::getCustomer(int index){
    return customers[index];
}
void Movie::print(){
    cout << name << endl;
}
int Movie::getIndex(){
    return currentIndex;
}
