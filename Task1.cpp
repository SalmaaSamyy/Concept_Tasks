#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <numeric> // For accumulate

using namespace std;

int main() {
    // Step 1: Accept input
    cout << "Enter daily steps separated by spaces: ";
    string input;
    getline(cin, input);

    // Step 2: Convert input to a vector of integers
    vector<int> steps;
    stringstream ss(input);
    int step;
    while (ss >> step) {
        steps.push_back(step);
    }

    // Step 3: Calculate required statistics
    int highest_steps = *max_element(steps.begin(), steps.end());
    int lowest_steps = *min_element(steps.begin(), steps.end());
    double average_steps = accumulate(steps.begin(), steps.end(), 0.0) / steps.size();
    sort(steps.begin(), steps.end(), greater<int>());

    // Step 4: Print the results
    cout << "Highest Steps: " << highest_steps << endl;
    cout << "Lowest Steps: " << lowest_steps << endl;
    cout << "Average Steps: " << average_steps << endl;
    cout << "Sorted Steps (Descending): ";
    for (int step : steps) {
        cout << step << " ";
    }
    cout << endl;

    return 0;
}
