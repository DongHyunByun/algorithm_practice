#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

#define INF 987654321
using namespace std;

int dist[101][101];

int main() {
	int n, m;
	cin >> n;
	cin >> m;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (i == j) {
				dist[i][j] = 0;
			}
			else {
				dist[i][j] = INF;
			}
		}
	}

	int a, b, c;
	for (int i = 0; i < m; i++) {
		cin >> a >> b >> c;
		dist[a][b] = min(dist[a][b],c);
	}

	for (int k = 1; k <= n; k++) {
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				if (dist[i][j] > dist[i][k] + dist[k][j]) {
					dist[i][j] = dist[i][k] + dist[k][j];
				}
			}
		}
	}

	

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (dist[i][j] == INF) {
				cout << 0<<" ";
			}
			else {
				cout << dist[i][j] << " ";
			}
		}
		cout << "\n";
	}

	return 0;
}