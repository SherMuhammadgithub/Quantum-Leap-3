v#include <iostream>
using namespace std;

class Node {
  public:
    int data;
    Node* next;
    Node(int val) {
        data = val;
        next = NULL;
    }
};

class Queue {
    Node *front, *rear;

  public:
    Queue() {
        front = rear = NULL;
    }

    // Function to add an element to the queue
    void enqueue(int val) {
        Node* newNode = new Node(val);
        if (rear == NULL) {
            front = rear = newNode;
            return;
        }
        rear->next = newNode;
        rear = newNode;
    }

    // Function to remove an element from the queue
    void dequeue() {
        if (front == NULL) {
            cout << "Queue is Empty\n";
            return;
        }
        Node* temp = front;
        front = front->next;
        if (front == NULL) {
            rear = NULL;
        }
        delete temp;
    }

    // Function to display the front element
    int peek() {
        if (front == NULL) {
            cout << "Queue is Empty\n";
            return -1;
        }
        return front->data;
    }

    // Function to display the queue
    void display() {
        if (front == NULL) {
            cout << "Queue is Empty\n";
            return;
        }
        Node* temp = front;
        while (temp != NULL) {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }
};

// Main function
int main() {
    Queue q;
    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);

    cout << "Queue after enqueuing: ";
    q.display();

    q.dequeue();    
    cout << "Queue after dequeuing: ";
    q.display();

    cout << "Front element is " << q.peek() << endl;

    return 0;
}
