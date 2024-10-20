#include <iostream>

template<typename T>
class ArrayList {
private:
    T* data;
    int size;
    int capacity;

public:
    ArrayList() : size(0), capacity(2) {
        data = new T[capacity];
    }

    void pushBack(T value) {
        if (size == capacity) {
            capacity = static_cast<int>(capacity * 1.5);
            T* newData = new T[capacity];
            for (int i = 0; i < size; i++)
                newData[i] = data[i];
            delete[] data;
            data = newData;
        }
        data[size++] = value;
    }

    T& operator[](int index) {
        return data[index];
    }

    friend std::ostream& operator<<(std::ostream& out, const ArrayList& arr) {
        for (int i = 0; i < arr.size; i++)
            out << arr.data[i] << " ";
        return out;
    }

    ~ArrayList() {
        delete[] data;
    }
};

int main() {
    ArrayList<int> arr;
    arr.pushBack(10);
    arr.pushBack(20);
    arr.pushBack(30);
    std::cout << arr;
    return 0;
}
