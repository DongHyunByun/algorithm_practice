#include <iostream>
#include <algorithm>

using namespace std;

long long pascal[1000][1000];

int main() {
	int N, K;
	int max = 10007;
	cin >> N >> K;

	for (int n = 0; n <= N; n++) {
		for (int k = 0; k <= n; k++) {
			if (k == 0) {
				pascal[n][k] = 1;
			}
			else {
				pascal[n][k] = pascal[n - 1][k] + pascal[n - 1][k - 1];
				if (pascal[n][k] > max) {
					pascal[n][k] = pascal[n][k] % max;
				}
			}
		}
	}

	cout << pascal[N][K] % max << endl;

	return 0;
}