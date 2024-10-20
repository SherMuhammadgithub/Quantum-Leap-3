#include <iostream>
using namespace std;


class Node{
  public :
  int data;
  Node *next;
  
  Node(){
    data = 0;
    next = nullptr;
  }
  
  Node(int data){
    this->data = data;
    this->next = nullptr;
  }
};

// linked list class
class LinkedList{
  Node *head;
  
  public:
    LinkedList(){
      head = NULL;
   }
  
  void insertAtHead(int data){
    Node *newNode = new Node(data);
    newNode->next = head;
    head = newNode;
  }
  
  void inserAtEnd(int data){
    Node *newNode = new Node(data);
    if(head == NULL){
      head = newNode;
      return;
    }
    
    Node *temp = head;
    while(temp->next != NULL){
      temp = temp->next;
    }
    
    temp->next = newNode;
    
  }
  
  bool findNode(int data){
    Node *temp = head;
    if(head == NULL){
      return false; // list empty no node found
    }
    
    while(temp != NULL){
      if(temp->data == data){
        return true; // node found
      }
      temp = temp->next;
    }
    
    return false;
  }
  
  void removeNode(int data){
    if(head == NULL){
      return; // no node exist 
    }
    Node *temp = head;
    Node *prev = nullptr;
    
    while(temp != NULL){
      if(temp->data == data){
        if(prev == nullptr){
          head = temp->next;
        } else{
          prev->next = temp->next;
        }
        delete temp;
      }
      
      prev = temp;
      temp = temp->next;
    }
    
    
  }
  
  bool deleteFromStart(){
    Node *temp = head;
    if(head == NULL){
      return false;
    }
  }
  
  void displayList(){
    Node *temp = this->head;
    if(head == NULL){
      std::cout << "List is empty" << std::endl;
      return;
    }
    
    while(temp != NULL){
      std::cout << temp->data << std::endl;
      temp = temp->next;
    }
  }
};
int main() 
{
  LinkedList list;
  list.insertAtHead(20);
  list.displayList();
  // 
  list.insertAtHead(10);
  list.displayList();
  
  list.inserAtEnd(0);
  
  list.displayList();
  
  std::cout << list.findNode(10) << std::endl;
  
  list.removeNode(10);
  
  list.displayList();
}