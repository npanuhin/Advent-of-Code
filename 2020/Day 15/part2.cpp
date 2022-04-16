#include <iostream>
#include <fstream>

using namespace std;


int nums[30'000'000];

int main() {
    fill_n(nums, 30'000'000, 0);

    ifstream in("input.txt");
    int i = 1, last, cur;
    char separator;

    while (in >> cur >> separator) nums[cur] = i++;
    in >> cur;

    for (int step = i; step < 30'000'000; ++step) {
        last = nums[cur];
        nums[cur] = step;
        cur = (last == 0 ? 0 : step - last);
    }

    cout << cur << endl;
}
