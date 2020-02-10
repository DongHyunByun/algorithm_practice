#include <iostream>
#include <algorithm>
#include <string.h>

using namespace std;

int L[1000];

// dp[i][j] : i~j�� �̾����� �ٿ찡 ���� �� �ִ� �ִ� ����
int dp[1001][1001];

int main() {	
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int t;
	cin >> t;
	for (int a = 0; a < t; a++) {
		int N;	
		cin >> N;
		memset(dp, 0, sizeof(dp));

		for (int i = 1; i <= N; i++) {
			cin >> L[i];
			if (N % 2 == 1) {
				dp[i][i] = L[i];
			}
		}

		for (int l = 1; l < N; l++) {
			for (int i = 1; i <= N - l; i++) {
				int j = i + l;

				// �ٿ�����
				if((N - (j - i + 1)) % 2 == 0) {
					dp[i][j] = max(dp[i + 1][j] + L[i], dp[i][j - 1] + L[j]);
				}
				// �������
				else {
					dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]);
				}

			}
		}
		cout << dp[1][N] << "\n";
	}

	return 0;
}