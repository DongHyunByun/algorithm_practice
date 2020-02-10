#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <utility>

#define maxV 501
#define maxE 6001
#define INF 987654321

using namespace std;

int N, M;
vector<int> edge[maxE];
int dist[maxV];

int main() {
	cin >> N >> M;

	for (int i = 1; i <= N; i++) {
		dist[i] = INF;
	}
 	dist[1] = 0;

	int A, B, C;
	for (int i = 0; i < M; i++) {
		cin >> A >> B >> C;
		edge[i] = { A,B,C };
	}
	
	// 최대 N번
	bool isChange;
	int from, to, cost;
	for (int i = 0; i < N; i++) {
		isChange = false;
		// 간선별 시작
		for (int e = 0; e < M; e++) {
			from=edge[e][0];
			to=edge[e][1];
			cost=edge[e][2];
			if (dist[from]!=INF and (cost + dist[from] < dist[to]) ) {
				isChange = true;
				dist[to] = cost + dist[from];
			}
		}
		if (!isChange) {
			break;
		}
	}
	//끝났는데도 음직이면
	if (isChange) {
		cout << -1;
	}
	else {
		for (int i = 2; i <= N; i++) {
			if (dist[i] == INF) {
				cout << -1 << "\n";
			}
			else {
				cout << dist[i] << "\n";
			}
		}
	}

	return 0;
}