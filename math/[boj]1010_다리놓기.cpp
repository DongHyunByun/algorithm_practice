#include <iostream>
#include <algorithm>

using namespace std;

long long pascal[30][30];

int main() {
	int t, N, M;

	for (int n = 0; n < 30; n++) {
		for (int k = 0; k <= n; k++) {
			if (n == 0 or n == k) {
				pascal[n][k] = 1;
			}
			else {
				pascal[n][k] = pascal[n - 1][k - 1] + pascal[n - 1][k];
			}
		}
	}

	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> N >> M;
		cout << pascal[M][N] << endl;
	}

	return 0;
}