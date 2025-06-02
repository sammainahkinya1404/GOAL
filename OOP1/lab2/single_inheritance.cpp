#include <iostream>
using namespace std;

class Student {
protected:
    string name;
    int rollNo;

public:
    void setStudent(string n, int r) {
        name = n;
        rollNo = r;
    }

    void displayStudent() {
        cout << "Name: " << name << ", Roll No: " << rollNo << endl;
    }
};

class GraduateStudent : public Student {
private:
    string thesisTitle;

public:
    void setThesis(string t) {
        thesisTitle = t;
    }

    void displayInfo() {
        displayStudent();
        cout << "Thesis Title: " << thesisTitle << endl;
    }
};

int main() {
    GraduateStudent g;
    g.setStudent("Alice", 42);
    g.setThesis("AI in Healthcare");
    g.displayInfo();
    return 0;
}
