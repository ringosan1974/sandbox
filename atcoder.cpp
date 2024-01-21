#include <iostream>
#include <string>
using namespace std;

int comb(int a, int b);

int main() {
    int n;
    int s;
    cin >> n;
    cin >> s;
    // "<"で文字列を区切り、">"の数 + 1 のnCrをとって、各ブロックを合計
    cout << comb(0, 3);
    return 0;
}

int comb(int a, int b) {
    int pa = 1;
    int pb = 1;
    for (int i = 1; i < b+1; ++i) {
        pa *= (a-i+1);
        pb *= i;
    }
    return pa / pb;
}