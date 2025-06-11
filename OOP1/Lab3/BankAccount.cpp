//Encapsulation is about binding data and functions together
// and restricting access to internal data using access specifiers (private, public, protected).
//Private members: accountHolder, balance are protected from outside interference.
//Public methods: Act as interfaces to interact safely.

#include <iostream>
#include <string>
using namespace std;

class BankAccount {
private:
    string accountHolder;
    double balance;

public:
    BankAccount(string name, double initialBalance) {
        accountHolder = name;
        balance = initialBalance;
    }

    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            cout << "Deposited: $" << amount << endl;
        } else {
            cout << "Invalid deposit amount!" << endl;
        }
    }

    void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            cout << "Withdrawn: $" << amount << endl;
        } else {
            cout << "Invalid withdraw amount!" << endl;
        }
    }

    void displayBalance() {
        cout << accountHolder << "'s Balance: $" << balance << endl;
    }
};

int main() {
    BankAccount acc("Alice", 500);
    acc.displayBalance();
    acc.deposit(200);
    acc.withdraw(150);
    acc.displayBalance();

    return 0;
}
