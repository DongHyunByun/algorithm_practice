#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int dp[1001][1001];

int main() {
	int n, m;
	cin >> n >> m;

	
	int ans = 0;
	string temp;
	for (int i = 1; i <= n; i++) {
		cin >> temp;
		for (int j = 1; j <= m; j++) {
			if (temp[j-1]=='1') {
				dp[i][j] = min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1;
				ans = max(ans, dp[i][j]);
			}
		}
	}

	cout << ans*ans;
	return 0;
}