#include "customerlist.h"
#include "iostream"

CustomerList::CustomerList()
{
    currentIndex = 0;
    maxCustomers = 100;
    customers = new Customer[maxCustomers];
}

void CustomerList::addCustomer(string cName, int cNumber){

    if(this->getCustomerByInfo(cName, cNumber) == nullptr){
        customers[currentIndex] = Customer(cName, cNumber);
        currentIndex++;
    }
}

void CustomerList::deleteCustomer(){
    //todo
}

void CustomerList::print(){
    for(int i = 0; i < currentIndex; i++){
        customers[i].printAll();
    }
}

Customer* CustomerList::getCustomerByInfo(string cName, int cNumber){
    for(int i = 0; i < currentIndex; i++){
        if(customers[i].getName() == cName || customers[i].getNumber() == cNumber)
            return &customers[i];
    }
    return nullptr;
}
