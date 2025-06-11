// One Interface, Many Forms
// 📘 Explanation:
// Use base class pointers to call derived class functions.

// Enable dynamic behavior using virtual.

#include <iostream>
using namespace std;

class Animal {
public:
    virtual void makeSound() {
        cout << "Some animal sound" << endl;
    }
};

class Dog : public Animal {
public:
    void makeSound() override {
        cout << "Bark!" << endl;
    }
};

class Cat : public Animal {
public:
    void makeSound() override {
        cout << "Meow!" << endl;
    }
};

int main() {
    Animal* a1 = new Dog();
    Animal* a2 = new Cat();
    
    a1->makeSound(); // Bark!
    a2->makeSound(); // Meow!

    delete a1;
    delete a2;
    return 0;
}
