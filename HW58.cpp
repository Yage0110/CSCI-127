//Agyei Bacchus
//agyei.bacchus92@myhunter.cuny.edu
//Birth date

#include <iostream>
using namespace std;

int main() {
    int yearBorn;
    
    do {
        cout << "Please enter the year born: ";
        cin >> yearBorn;

        if (yearBorn > 2018) {
            cout << "Entered a future year" << endl;
        }
    } while (yearBorn > 2018);

    cout << "You entered: " << yearBorn << endl;

    return 0;
}
