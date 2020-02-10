#include <iostream>
#include <utility>
#include <vector>
#include <queue>
#include <functional>

#define INF 987654321

using namespace std;
int N, M, S, D;

// dist[i][j] : i에서 j까지 최단거리 (i와 j는 인접한 노드)
long long dist[500][500];

// dist2[i] : s에서 i 노드까지의 최단거리
long long dist2[500];

void dijs() {
	for (int i = 0; i < N; i++) {
		dist2[i] = INF;
	}
	dist2[S] = 0;
	// { {최단거리,노드} }
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	pq.push({ 0,S });

	while (!pq.empty()) {
		int cost = pq.top().first;
		int nowV = pq.top().second;
		pq.pop();

		for (int i = 0; i < N; i++) {
			/*
			if (dist[nowV][i] == INF) {
				continue;
			}
			*/
			if (dist2[i] > cost + dist[nowV][i]) {
				dist2[i] = cost + dist[nowV][i];
				pq.push({ dist2[i],i });
			}
		}
	}
}

int main() {
	cin.tie(NULL);
	cout.tie(NULL);

	while (1) {
		cin >> N >> M;
		if (N == 0 && M == 0) {
			break;
		}
		// test case 시작
		else {
			// 시작점 끝점
			cin >> S >> D;

			// edge 초기화 및 채우기
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {

					dist[i][j] = INF;

				}
			}
			int U, V, P;
			for (int e = 0; e < M; e++) {
				cin >> U >> V >> P;
				dist[U][V] = P;
			}

			// 최단거리 찾기
			dijs();

			// 도착지에서 역으로 탐색하며 최단거리 지우기
			queue<int> q;
			q.push(D);
			while (!q.empty()) {
				int nowNode = q.front(); q.pop();
				for (int i = 0; i < N; i++) {
					/*
					if (dist[i][nowNode] == INF) {
						continue;
					}
					*/
					// 최단경로중 하나
					if (dist2[nowNode] == dist[i][nowNode] + dist2[i]) {
						dist[i][nowNode] = INF;
						q.push(i);
					}
				}
			}

			// 최단거리를 제외하고 최단거리찾기
			dijs();

			if (dist2[D] == INF) {
				cout << -1 << "\n";
			}
			else {
				cout << dist2[D] << "\n";
			}

		}
	}
	return 0;
}