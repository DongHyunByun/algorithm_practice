#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int dp[4001][4001];

int main() {
	string A, B;
	cin >> A >> B;

	int sizeA = A.size();
	int sizeB = B.size();
	int ans = 0;

	for (int i = 1; i <= sizeA; i++) {
		for (int j = 1; j <= sizeB; j++) {
			if (A[i - 1] == B[j - 1]) {
				dp[i][j]=dp[i - 1][j - 1] + 1;
				if (ans < dp[i][j]) {
					ans = dp[i][j];
				}
			}
		}
	}
	cout << ans;
	return 0;
}