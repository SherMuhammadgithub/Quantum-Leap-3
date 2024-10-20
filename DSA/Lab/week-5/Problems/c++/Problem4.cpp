#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main() {
    vector<int> vec = {50, 40, 30, 20, 10, 10, 20};

    // Reverse the vector
    reverse(vec.begin(), vec.end());
    cout << "Reversed Vector: ";
    for (int v : vec)
        cout << v << " ";
    cout << endl;

    // Sort the vector
    sort(vec.begin(), vec.end());
    cout << "Sorted Vector: ";
    for (int v : vec)
        cout << v << " ";
    cout << endl;

    // Remove duplicates using a set
    set<int> uniqueSet(vec.begin(), vec.end());
    vec.assign(uniqueSet.begin(), uniqueSet.end());
    cout << "After Removing Duplicates: ";
    for (int v : vec)
        cout << v << " ";
    cout << endl;

    return 0;
}
