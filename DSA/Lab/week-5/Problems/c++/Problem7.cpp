#include <iostream>

template<typename T>
class Vector {
private:
    T* data;
    int size;
    int capacity;

public:
    Vector() : size(0), capacity(1) {
        data = new T[capacity];
    }

    void pushBack(T value) {
        if (size == capacity) {
            capacity *= 2;
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

    friend std::ostream& operator<<(std::ostream& out, const Vector& vec) {
        for (int i = 0; i < vec.size; i++)
            out << vec.data[i] << " ";
        return out;
    }

    ~Vector() {
        delete[] data;
    }
};

int main() {
    Vector<int> vec;
    vec.pushBack(10);
    vec.pushBack(20);
    vec.pushBack(30);
    std::cout << vec;
    return 0;
}
