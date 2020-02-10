#include <iostream>
#include <algorithm>

using namespace std;

int N;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> N;
	int divider=2;
	while (N!=1) {
		if (N%divider == 0) {
			N = N / divider;
			cout << divider << "\n";
		}
		else {
			divider++;
		}
	}
	return 0;
}