#include <iostream>
using namespace std;

class Car {
private:
    string brand;

public:
    Car(string b) {
        brand = b;
        cout << "Car object for " << brand << " created." << endl;
    }

    ~Car() {
        cout << "Car object for " << brand << " destroyed." << endl;
    }

    void showBrand() {
        cout << "Brand: " << brand << endl;
    }
};

int main() {
    Car c1("Toyota");
    c1.showBrand();
    return 0;
}
