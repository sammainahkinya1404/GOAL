#include <iostream>
using namespace std;

class Animal {
protected:
    string name;

public:
    void setName(string n) {
        name = n;
    }

    void speak() {
        cout << name << " makes a sound." << endl;
    }
};

class Dog : public Animal {
public:
    void bark() {
        cout << name << " barks." << endl;
    }
};

int main() {
    Dog d;
    d.setName("Buddy");
    d.speak();
    d.bark();
    return 0;
}
