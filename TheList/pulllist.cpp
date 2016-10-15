#include "pulllist.h"
#include <fstream>

using namespace std;


PullList::PullList(MovieList& mList, CustomerList& cList){



}

void PullList::pull(MovieList& mList, CustomerList& cList){
    ifstream input("topull.txt");

    if(!input.is_open()){
        cout << "Error opening file!!!";
        exit(0);
    }
    int numMovies;
    input >> numMovies;

    toBePulled = new string*[numMovies];
    for(int i = 0; i < numMovies; i++)
        toBePulled[i] = new string[2];

    for(int i = 0; i < numMovies; i++){
        input >> toBePulled[i][0] >> toBePulled[i][1];
        for(int j = 0; j < mList.getCurrentIndex(); j ++){
            if(toBePulled[i][0] == mList.getMoviebyIndex(j)->getName()){
                pullMovies.addMovie(mList.getMoviebyIndex(j)->getName());
                int temp1 =  mList.getMoviebyIndex(j)->getIndex();
                //cout << temp1;
                //cout << atoi(toBePulled[i][1].c_str());
                for(int k = 0; k < min(atoi(toBePulled[i][1].c_str()), temp1); k++){
                    pullCust.addCustomer(mList.getMoviebyIndex(j)->getCustomer(0)->getName(), mList.getMoviebyIndex(j)->getCustomer(0)->getNumber());
                   // cout << pullCust.getCustomerByInfo(mList.getMoviebyIndex(j)->getCustomer(0)->getName(), mList.getMoviebyIndex(j)->getCustomer(0)->getNumber())->getName() << endl;
                    pullMovies.getMoviebyIndex(i)->addCustomer(pullCust.getCustomerByInfo(mList.getMoviebyIndex(j)->getCustomer(0)->getName(), mList.getMoviebyIndex(j)->getCustomer(0)->getNumber()));
                    mList.getMoviebyIndex(j)->deleteCustomer(0);
                }
            }
        }
    }
    ifstream srce( "list.txt", ios::binary );
    ofstream dest ( "backup\\listbackup.txt", ios::binary );
    dest << srce.rdbuf();
    pullCust.print();
    delete toBePulled;
}
