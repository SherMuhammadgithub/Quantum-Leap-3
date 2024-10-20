#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    vector<string> vec;
    int choice;
    string str;

    do {
        cout << "\n1. Add string\n2. Remove last string\n3. Display vector\n4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter string to add: ";
                cin >> str;
                vec.push_back(str);
                break;
            case 2:
                if (!vec.empty()) {
                    vec.pop_back();
                    cout << "Last string removed.\n";
                } else {
                    cout << "Vector is empty.\n";
                }
                break;
            case 3:
                cout << "Vector elements: ";
                for (const auto &s : vec)
                    cout << s << " ";
                cout << "\nSize: " << vec.size() << ", Capacity: " << vec.capacity() << endl;
                break;
        }
    } while (choice != 4);

    return 0;
}
