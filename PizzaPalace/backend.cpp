#include "httplib.h"
#include "json.hpp"
#include <iostream>

using json = nlohmann::json;

int main() {
    httplib::Server svr;

    // Endpoint to get the menu
    svr.Get("/menu", [](const httplib::Request& req, httplib::Response& res) {
        json menu = {
            {"Pizza", 10.00},
            {"Soda", 2.00},
            {"Chicken Nuggets", 5.00},
            {"Breadsticks", 3.00}
        };
        res.set_content(menu.dump(), "application/json");
    });

    // Endpoint to place an order
    svr.Post("/placeOrder", [](const httplib::Request& req, httplib::Response& res) {
        auto order = json::parse(req.body);
        double subtotal = 0.0;

        // Calculate subtotal
        for (const auto& item : order["items"]) {
            if (item == "Pizza") subtotal += 10.00;
            else if (item == "Soda") subtotal += 2.00;
            else if (item == "Chicken Nuggets") subtotal += 5.00;
            else if (item == "Breadsticks") subtotal += 3.00;
        }

        // Calculate tax and total
        double tax = subtotal * 0.08; // 8% tax
        double total = subtotal + tax;

        // Generate receipt
        json receipt = {
            {"items", order["items"]},
            {"subtotal", subtotal},
            {"tax", tax},
            {"total", total}
        };
        res.set_content(receipt.dump(), "application/json");
    });

    std::cout << "Server running at http://localhost:8080\n";
    svr.listen("localhost", 8080);
}