#include <iostream>

int main() {
    int pizzaQty, sodaQty, nuggetsQty;
    double total = 0.0;
    const double TAX_RATE = 0.08;

    std::cin >> pizzaQty >> sodaQty >> nuggetsQty;

    total += pizzaQty * 10;  // Pizza = $10 each
    total += sodaQty * 2;    // Soda = $2 each
    total += nuggetsQty * 5; // Nuggets = $5 each

    total *= (1 + TAX_RATE); // Apply 8% tax

    std::cout << total; // Return total to Python
    return 0;
}
