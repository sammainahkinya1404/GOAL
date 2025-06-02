#include <iostream>
using namespace std;

class Person {
protected:
    string name;

public:
    void setName(string n) {
        name = n;
    }
};

class Employee : public Person {
protected:
    int empID;

public:
    void setEmpID(int id) {
        empID = id;
    }
};

class Manager : public Employee {
private:
    string department;

public:
    void setDepartment(string dept) {
        department = dept;
    }

    void displayManager() {
        cout << "Name: " << name << ", ID: " << empID << ", Department: " << department << endl;
    }
};

int main() {
    Manager m;
    m.setName("John");
    m.setEmpID(1001);
    m.setDepartment("Finance");
    m.displayManager();
    return 0;
}
