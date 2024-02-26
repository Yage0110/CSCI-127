//Agyei Bacchus
//agyei.bacchus92@myhunter.cuny.edu
//Population

#include <iostream>
using namespace std;

int main() {
    double population = 325.7;
    double birthRate = 12.4 / 1000;  
    double deathRate = 8.4 / 1000;

    int years;
    cout << "Please enter the number of years: ";
    cin >> years;

    cout << "Year\tPopulation (in millions)" << endl;

    for (int i = 0; i <= years; ++i) {
        cout << "Year " << 2017 + i << "\t" << population << endl;
        population = population + (birthRate * population) - (deathRate * population);
    }

    return 0;
}

