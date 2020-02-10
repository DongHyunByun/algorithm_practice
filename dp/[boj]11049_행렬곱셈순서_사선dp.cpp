#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

// dp[i][j] : i에서 j행렬까지의 곱중 최소연산
int dp[501][501];

// list[i][0] : i행렬의 행, list[i][1] : i행렬의 열
int list[501][2];

int main() {
	int N;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> list[i][0] >> list[i][1];
	}
	
	for (int l = 1; l <= N-1; l++) {
		for (int i = 1; i <= N - l; i++) {
			int j = i + l;
			for (int k = i; k < j; k++) {
				int c = dp[i][k] + dp[k + 1][j] + (list[i][0] * list[k][1] * list[j][1]);
				if (dp[i][j] == 0 || dp[i][j] > c) {
					dp[i][j] = c;
				}
			}
		}
	}
	/* dp확인
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cout << dp[i][j] << " ";
		}
		cout << endl;
	}
	*/

	cout << dp[1][N];
	return 0;
}