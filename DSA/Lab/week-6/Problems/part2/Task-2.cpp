#include <iostream>
#include <stack>
#include <string>
#include <sstream>
using namespace std;

bool isOperator(const string& input) {
    return input == "+" || input == "-" || input == "*" || input == "/" || input == "%";
}

int performOperation(const string& operation, int operand1, int operand2) {
    if (operation == "+") return operand1 + operand2;
    if (operation == "-") return operand1 - operand2;
    if (operation == "*") return operand1 * operand2;
    if (operation == "/") return operand1 / operand2;
    if (operation == "%") return operand1 % operand2;
    throw invalid_argument("Unknown operation");
}

int main() {
    stack<int> st;
    string input;

    while (true) {
        cout << "Enter operand/operator (postfix) or special commands (? for stack, ^ for top, ! to exit): ";
        cin >> input;

        // Handle exit condition
        if (input == "!") {
            cout << "Exiting the program." << endl;
            break;
        }

        // Handle stack display
        if (input == "?") {
            stack<int> temp = st;
            cout << "Stack: ";
            while (!temp.empty()) {
                cout << temp.top() << " ";
                temp.pop();
            }
            cout << endl;
            continue;
        }

        // Handle top display
        if (input == "^") {
            if (!st.empty()) {
                cout << "Top element: " << st.top() << endl;
                st.pop();
            } else {
                cout << "Stack is empty" << endl;
            }
            continue;
        }

        // Handle operators
        if (isOperator(input)) {
            if (st.size() < 2) {
                cout << "Error: Not enough operands" << endl;
                continue;
            }
            int operand2 = st.top(); st.pop();
            int operand1 = st.top(); st.pop();
            int result = performOperation(input, operand1, operand2);
            st.push(result);
            cout << "Performed " << operand1 << " " << input << " " << operand2 << " = " << result << endl;
            continue;
        }

        // Handle integer input
        try {
            int operand = stoi(input);
            st.push(operand);
        } catch (invalid_argument&) {
            cout << "Invalid input" << endl;
        }
    }

    return 0;
}
