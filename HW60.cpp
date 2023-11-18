//Jay Bacchus
//agyei.bacchus92@myhunter.cuny.edu
//Two's complement
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter a whole number between -31 and 31: ";
    cin >> n;

    int x;
    if (n < 0) {
        cout << "1";
        x = 32 + n;
    } else {
        cout << "0";
        x = n;
    }

    int b = 16;
    while (b > 0.5) {
        if (x >= b) {
            cout << "1";
            x %= b;
        } else {
            cout << "0";
        }
        b /= 2;
    }

    cout << "\n";

    return 0;
}
