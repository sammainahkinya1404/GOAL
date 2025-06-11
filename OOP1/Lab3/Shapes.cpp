//Abstraction means hiding complex implementation and showing only essential features. 
//This is best done using abstract classes or interfaces.
#include <iostream>
#include <cmath>
using namespace std;

// Abstract Class
class Shape {
public:
    virtual double area() = 0;  // Pure virtual function
    virtual void display() = 0;
};

class Circle : public Shape {
private:
    double radius;
public:
    Circle(double r) { radius = r; }

    double area() override {
        return M_PI * radius * radius;
    }

    void display() override {
        cout << "Circle Area: " << area() << endl;
    }
};

class Rectangle : public Shape {
private:
    double length, width;
public:
    Rectangle(double l, double w) {
        length = l;
        width = w;
    }

    double area() override {
        return length * width;
    }

    void display() override {
        cout << "Rectangle Area: " << area() << endl;
    }
};

int main() {
    Shape* s1 = new Circle(5.0);
    Shape* s2 = new Rectangle(4.0, 6.0);

    s1->display();
    s2->display();

    delete s1;
    delete s2;

    return 0;
}
