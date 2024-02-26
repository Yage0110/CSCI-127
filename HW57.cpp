//Agyei Bacchus
//agyei.bacchus92@myhunter.cuny.edu
//Time of year
#include <iostream>
using namespace std;

int main() {
    int month;
    cout << "Enter the month of the year (as a number): ";
    cin >> month;

    if (month < 3 || month > 11) {
        cout << "Happy Winter";
    } else if (month >= 3 && month < 7) {
        cout << "Happy Spring";
    } else if (month >= 7 && month < 9) {
        cout << "Happy Summer";
    } else {
        cout << "Happy Fall";
    }

    cout << endl;

    return 0;
}
