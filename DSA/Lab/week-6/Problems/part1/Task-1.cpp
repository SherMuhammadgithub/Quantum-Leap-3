#include <iostream>
using namespace std;

// Node class to represent a node of the linked list
class Node {
  public:
    int data;
    Node *next;

    // Default constructor
    Node() {
        data = 0;
        next = NULL;
    }

    // Parameterized Constructor
    Node(int data) {
        this->data = data;
        this->next = NULL;
    }
};

// Linked list class to implement a singly linked list
class LinkedList {
    Node *head;

  public:
    // Default constructor
    LinkedList() {
        head = NULL;
    }

    // Destructor to delete the list
    ~LinkedList() {
        while (head != NULL) {
            Node *temp = head;
            head = head->next;
            delete temp;
        }
    }

    // Function to insert a node at the start of the linked list
    void insertAtHead(int data) {
        Node *newNode = new Node(data);
        newNode->next = this->head;
        this->head = newNode;
    }

    // Function to insert a node at the end of the linked list
    void insertAtEnd(int data) {
        Node *newNode = new Node(data);
        if (head == NULL) {
            head = newNode;
            return;
        }
        Node *temp = head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
    }

    // Function to search for a value in the list
    bool findNode(int data) {
        Node *temp = head;
        while (temp != NULL) {
            if (temp->data == data) {
                return true;
            }
            temp = temp->next;
        }
        return false;
    }

    // Function to delete a node from the list
    void deleteNode(int data) {
        if (head == NULL) return;

        Node *temp = head;

        // If the node to be deleted is the head
        if (head->data == data) {
            head = head->next;
            delete temp;
            return;
        }

        Node *prev = NULL;
        while (temp != NULL && temp->data != data) {
            prev = temp;
            temp = temp->next;
        }

        // Node not found
        if (temp == NULL) return;

        // Unlink the node and delete
        prev->next = temp->next;
        delete temp;
    }

    // Function to reverse the linked list
    void reverseList() {
        Node *prev = NULL, *current = head, *next = NULL;
        while (current != NULL) {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        head = prev;
    }

    // Function to display the linked list
    void print() {
        Node *temp = head;
        if (head == NULL) {
            cout << "List empty" << endl;
            return;
        }
        while (temp != NULL) {
            cout << temp->data << " ";
            temp = temp->next;
        }
    }
};

// Main function
int main() {
    // Creating a LinkedList object
    LinkedList list;

    // Inserting nodes at the head
    list.insertAtHead(4);
    list.insertAtHead(3);
    list.insertAtHead(2);
    list.insertAtHead(1);

    // Inserting a node at the end
    list.insertAtEnd(5);

    // Printing the list
    cout << "Elements of the list are: ";
    list.print();
    cout << endl;

    // Searching for a node
    cout << "Finding 3 in the list: " << (list.findNode(3) ? "Found" : "Not Found") << endl;

    // Deleting a node
    list.deleteNode(3);
    cout << "List after deleting 3: ";
    list.print();
    cout << endl;

    // Reversing the list
    list.reverseList();
    cout << "List after reversing: ";
    list.print();
    cout << endl;

    return 0;
}
