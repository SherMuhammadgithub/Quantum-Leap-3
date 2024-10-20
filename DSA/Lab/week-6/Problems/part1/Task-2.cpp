#include <iostream>
#define MAX 1000
using namespace std;

class Stack {
    int top;

  public:
    int arr[MAX]; // Maximum size of Stack

    // Default constructor
    Stack() { top = -1; }

    // Function to add an element to the stack
    bool push(int x) {
        if (top >= (MAX - 1)) {
            cout << "Stack Overflow\n";
            return false;
        } else {
            arr[++top] = x;
            cout << x << " pushed into stack\n";
            return true;
        }
    }

    // Function to remove an element from the stack
    int pop() {
        if (top < 0) {
            cout << "Stack Underflow\n";
            return 0;
        } else {
            int x = arr[top--];
            return x;
        }
    }

    // Function to return the top element of the stack
    int peek() {
        if (top < 0) {
            cout << "Stack is Empty\n";
            return 0;
        } else {
            int x = arr[top];
            return x;
        }
    }

    // Function to check if the stack is empty
    bool isEmpty() {
        return (top < 0);
    }
};

// Main function
int main() {
    Stack stack;
    stack.push(10);
    stack.push(20);
    stack.push(30);

    cout << stack.pop() << " popped from stack\n";
    cout << "Top element is " << stack.peek() << endl;

    return 0;
}
