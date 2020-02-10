#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int dp[2][302];
int stair[302];

int main() {	
	int N;
	cin >> N;

	for (int i = 2; i < N+2; i++) {
		cin >> stair[i];
	}
	
	dp[1][N+1] = stair[N + 1];

	for (int j = N + 1; j > 1; j--) {
		if (dp[0][j] != 0) {
			dp[1][j-2] = max(dp[1][j-2], dp[0][j] + stair[j - 2]);
		}
		if (dp[1][j] != 0) {
			dp[0][j-1] = max(dp[0][j-1], dp[1][j] + stair[j - 1]);
			dp[1][j-2] = max(dp[1][j-2], dp[1][j] + stair[j - 2]);
		}
	}

	/*
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < N+2; j++) {
			cout << dp[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
	*/

	cout << max(max(dp[0][0], dp[0][1]), max(dp[1][0], dp[1][1]));

	return 0;
}