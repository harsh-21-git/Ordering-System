#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <cctype>
using namespace std;

// Constants
const double TAX_RATE = 0.08; // 8% sales tax

// Function Prototypes
void displayMenu(const vector<string>& items, const vector<double>& prices);
void generateReceipt(const vector<string>& items, const vector<double>& prices, const vector<int>& quantities, double tax, double total);

int main() {
    // Menu items and prices
    vector<string> menuItems = {"Pizza", "Soda", "Chicken Nuggets", "Breadsticks"};
    vector<double> menuPrices = {15.50, 2.00, 7.00, 9.75};
    vector<int> quantities(menuItems.size(), 0); // Tracks quantity of each item ordered

    char itemLetter;
    double total = 0.0;

    cout << "=====================================================\n"
         << "\t\tWelcome to Pizza Palace\n"
         << "=====================================================" << endl;

    do {
        displayMenu(menuItems, menuPrices);

        // Get user input
        cout << "Please select a menu item (A-" << char('A' + menuItems.size() - 1) << ") or E to Exit: ";
        cin >> itemLetter;
        itemLetter = toupper(itemLetter);

        if (itemLetter == 'E') {
            break;
        }

        // Validate menu selection
        int index = itemLetter - 'A';
        if (index < 0 || index >= menuItems.size()) {
            cerr << "\nInvalid selection. Please try again.\n";
            continue;
        }

        // Get quantity
        int quantity = 0;
        cout << "Enter quantity for " << menuItems[index] << ": ";
        while (!(cin >> quantity) || quantity <= 0) {
            cerr << "Invalid input. Please enter a positive number: ";
            cin.clear();
            cin.ignore(1000, '\n');
        }

        // Update quantities and total
        quantities[index] += quantity;
        total += menuPrices[index] * quantity;

        cout << "\nAdded " << quantity << " " << menuItems[index] << "(s) to your order.\n"
             << "Current total: $" << fixed << setprecision(2) << total << endl;

    } while (true);

    // Calculate tax and final total
    double tax = total * TAX_RATE;
    double finalTotal = total + tax;

    // Generate receipt
    generateReceipt(menuItems, menuPrices, quantities, tax, finalTotal);

    return 0;
}

// Function to display the menu
void displayMenu(const vector<string>& items, const vector<double>& prices) {
    cout << "\n-----------------------------------------------------\n"
         << "\t\tMenu\n"
         << "-----------------------------------------------------" << endl;

    for (size_t i = 0; i < items.size(); i++) {
        cout << "\t" << char('A' + i) << "\t" << left << setw(20) << items[i]
             << right << setw(10) << fixed << setprecision(2) << prices[i] << endl;
    }
    cout << "\tE\tExit\n"
         << "-----------------------------------------------------\n";
}

// Function to generate and display the receipt
void generateReceipt(const vector<string>& items, const vector<double>& prices, const vector<int>& quantities, double tax, double total) {
    cout << "\n=====================================================\n"
         << "\t\tPizza Palace Receipt\n"
         << "=====================================================\n"
         << left << setw(20) << "Item"
         << setw(10) << "Qty"
         << setw(15) << "Price"
         << setw(15) << "Subtotal" << endl;

    cout << "-----------------------------------------------------\n";

    for (size_t i = 0; i < items.size(); i++) {
        if (quantities[i] > 0) {
            cout << left << setw(20) << items[i]
                 << setw(10) << quantities[i]
                 << setw(15) << fixed << setprecision(2) << prices[i]
                 << setw(15) << prices[i] * quantities[i] << endl;
        }
    }

    cout << "-----------------------------------------------------\n"
         << right << setw(35) << "Tax: " << setw(15) << fixed << setprecision(2) << tax << endl
         << right << setw(35) << "Total: " << setw(15) << fixed << setprecision(2) << total << endl
         << "=====================================================\n"
         << "Thank you for dining with us! We hope to see you again!\n";
}
