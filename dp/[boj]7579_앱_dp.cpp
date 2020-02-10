#include <iostream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

#define maxCost 10001
using namespace std;


// dp[i][c] : i��° �۱��� ���� �� �ְ�, c������ �� �� ���� �� �ִ� �޸�
int dp[101][maxCost];

// m[i] : i��° ���� �޸�
int m[101];

// c[i] : i��° ���� cost
int c[101];

int main() {
	int N, M;
	cin >> N >> M;
	for (int i = 1; i <= N; i++) {
		cin >> m[i];
	}
	for (int i = 1; i <= N; i++) {
		cin >> c[i];
	}

	int ans = maxCost;
	for (int item = 1; item <= N; item++) {
		for (int cost = 0; cost < maxCost; cost++) {
			// item���� �� ���� ��
			if (cost >= c[item]) {
				// item-1 ���� ���� �� �ִ� ���¿��� ��
				dp[item][cost] = max(dp[item - 1][cost], dp[item - 1][cost - c[item]]+m[item]);
			}
			else {
				dp[item][cost] = dp[item - 1][cost];
			}
			if (dp[item][cost] >= M and cost<ans) {
				ans = cost;
			}
		}
	}
	/*
	//���Ȯ��
	for (int i = 0; i <= N; i++) {
		for (int j = 0; j < 80; j++) {
			cout << dp[i][j] << " ";
		}
		cout << endl;
	}
	*/

	cout << ans;

	return 0;
}