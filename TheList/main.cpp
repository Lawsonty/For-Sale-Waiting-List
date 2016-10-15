#include <iostream>
#include <fstream>

using namespace std;


#include"customer.h"
#include "movielist.h"
#include "customerlist.h"
#include "pulllist.h"

/*
 * This program is designed for use at the video store Wallace Video.
 * It keeps a list for each movie of who wants to buy a movie. When the
 * movies become available, it can be used to output a list of pulled
 * movies organized by customer.
 *
 * @author: Tyler Lawson
 */

//add more notes dummy

void save(CustomerList &clist, MovieList &mlist);

int main()
{
    ifstream input("list.txt");

    if(!input.is_open()){
        cout << "Error opening file!!!";
        exit(0);
    }
    CustomerList cList;
    MovieList mList;

    int temp1;
    int temp2;
    input >> temp1;
    for (int i = 0; i < temp1; i++){
        input >> temp2;
        string movieName;
        input >> movieName;

        mList.addMovie(movieName);
        for (int j = 0; j < temp2; j++){
            string customerName;
            int customerNumber;
            input >> customerName >> customerNumber;
            cList.addCustomer(customerName, customerNumber);
            mList.getMoviebyIndex(i)->addCustomer(cList.getCustomerByInfo(customerName, customerNumber));

        }
    }
//    mList.print();
//    cout << endl;
//    cList.print();
//    cout << endl;
//    mList.getMoviebyIndex(0)->getCustomer(0)->setName("Frank");

//    mList.print();
//    cout << endl;
//    cList.print();
//    cout << endl;

    PullList pList(mList, cList);
//    pList.pull(mList, cList);

//    mList.print();
//    cout << endl;


    int choice;
    int choice1;
    string temp;

    while (choice != 4){

        cout << "1)View Movie 2)Add Movie 3)Pull Movies 4)Exit" << endl;
        cin >> choice;
        switch(choice){
        case 1: for (int i = 0; i < mList.getCurrentIndex(); i++)
                    cout << i + 1 << ") " << mList.getMoviebyIndex(i)->getName() << endl;

                cout << "Select a Movie: ";
                cin >> choice;
                choice1 = 0;
                while(choice1 != 3){
                cout << mList.getMoviebyIndex(choice - 1)->getName() << endl;
                for (int i = 0; i < mList.getMoviebyIndex(choice - 1)->getIndex(); i++){
                    cout << i + 1 << ") ";
                    mList.getMoviebyIndex(choice - 1)->getCustomer(i)->print();
                }
                cout << "1)Add Person 2)Remove Person 3)Back" << endl;
                cin >> choice1;
                switch (choice1) {

                case 1: cout << "Enter Name and Number: ";
                        cin >> temp >> temp1;
                        cList.addCustomer(temp, temp1);
                        mList.getMoviebyIndex(choice - 1)->addCustomer(cList.getCustomerByInfo(temp, temp1));

                        save(cList, mList);//add person
                    break;
                case 2: cout << "Enter Index: ";
                        cin >> temp1;
                        mList.getMoviebyIndex(choice - 1)->deleteCustomer(temp1 - 1);

                        save(cList, mList);//remove person
                    break;
                case 3: break;//back
                }
              }
            break;//view movie
        case 2:
            cin >> temp;
            mList.addMovie(temp);
            //add movie
            break;
        case 3:
                pList.pull(mList, cList);//pull movies
                save(cList, mList);
            break;
        case 4: break;// exit
        }
    }

    return 0;
}

//This function should be used to update list.txt
void save(CustomerList &clist, MovieList &mlist){
    ofstream myfile ("list.txt", ios::trunc);
    if (myfile.is_open()){
        cout << "Saving Movies" << endl;
        myfile << mlist.getCurrentIndex() << endl;
        for (unsigned int i = 0; i < mlist.getCurrentIndex(); i++){
            if (mlist.getMoviebyIndex(i)->getIndex() != 0){
                myfile << mlist.getMoviebyIndex(i)->getIndex() << " " << mlist.getMoviebyIndex(i)->getName() << endl;
                for (unsigned int k = 0; k < mlist.getMoviebyIndex(i)->getIndex(); k++){
                    myfile << mlist.getMoviebyIndex(i)->getCustomer(k)->getName() << " " << mlist.getMoviebyIndex(i)->getCustomer(k)->getID() << endl;
                }
            }
        }
    }
    myfile.close();

}
