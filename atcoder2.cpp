#include <algorithm>
#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int main() {
    long int n;
    long int d;
    long int amin;
    long int sum = 0;
    long int ans[n];
    long int aati;
    vector<long int> a;
    cin >> n;
    for (int i = 0; i < n; ++i) {
		cin >> d;
		a.push_back(d);
	}
    sort(a.begin(), a.end());
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            aati = a.at(j);
            if (aati >= a.at(i) * (a.size()-i)) {
                sum += a.at(j);
            }
        }
        ans[i] = sum;
        cout << ans[i];
    }
    cout << endl;

    return 0;
}