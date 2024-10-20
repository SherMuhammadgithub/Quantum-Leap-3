#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> vec;

    for (int i = 1; i <= 100; i++) {
        vec.push_back(i);
        cout << "Inserted: " << i << ", Size: " << vec.size() << ", Capacity: " << vec.capacity() << endl;
    }

    return 0;
}