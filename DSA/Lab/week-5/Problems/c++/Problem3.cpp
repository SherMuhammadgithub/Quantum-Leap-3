#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> vec = {10, 20, 30, 40, 50};
    int searchValue, index = -1;

    cout << "Enter integer to search: ";
    cin >> searchValue;

    for (int i = 0; i < vec.size(); ++i) {
        if (vec[i] == searchValue) {
            index = i;
            break;
        }
    }

    if (index != -1)
        cout << "Integer found at index: " << index << endl;
    else
        cout << "Integer not found.\n";

    return 0;
}
