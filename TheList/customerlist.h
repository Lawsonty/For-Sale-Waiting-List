#ifndef CUSTOMERLIST_H
#define CUSTOMERLIST_H

#include "customer.h"

class CustomerList
{
public:
    CustomerList();

    void addCustomer(string cName, int cNumber);
    void deleteCustomer();
    void print();
    Customer* getCustomerByInfo(string cName, int cNumber);

private:
    Customer* customers;
    int maxCustomers;
    int currentIndex;
};

#endif // CUSTOMERLIST_H
