#include <iostream>
#include <stack>
#include <string>
using namespace std;

void reverseWords(const string& sentence) {
    stack<char> st;

    // Traverse through each character in the sentence
    for (int i = 0; i < sentence.length(); i++) {
        // If the current character is not a space, push it onto the stack
        if (sentence[i] != ' ') {
            st.push(sentence[i]);
        } else {
            // If a space is encountered, pop and print all characters from the stack
            while (!st.empty()) {
                cout << st.top();
                st.pop();
            }
            // Print the space after the word
            cout << " ";
        }
    }

    // Print the last word (characters remaining in the stack) 
    while (!st.empty()) {   
        cout << st.top();
        st.pop();
    }
    cout << endl;
}

int main() {
    string sentence = "I am from University of Engineering and Technology Lahore";
    cout << "Original Sentence: " << sentence << endl;
    cout << "Reversed Words: ";
    reverseWords(sentence);
    return 0;
}
