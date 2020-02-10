#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <utility>

#define INF 987654321
#define max_v 20001
#define max_e 300001

using namespace std;
int V, E;

// graph[i]={j,w}  : i 에서 j노드로 가는 가중치 w
vector<pair<int, int>> graph[max_v];

int dist[max_v];
// distance[j] : 출발노드에서 j노드까지의 거리, 초기엔 모두 INF
void dijst(int start) {
	for (int i = 1; i <= V; i++) {
		dist[i] = INF;
	}
	dist[start] = 0;

	// pq는 <cost, nowNode>, 초기값 설정
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	pq.push({ 0, start });

	int cost, currentV;
	while (!pq.empty()) {
		cost = pq.top().first;
		currentV = pq.top().second;
		pq.pop();

		//이미더 작은경우 패스
		if (dist[currentV] < cost) {
			continue;
		}

		// 연결노드 탐색
		int s = graph[currentV].size();
		for (int i = 0; i < s; i++) {
			int toNode = graph[currentV][i].first;
			int w = graph[currentV][i].second + cost;

			if (dist[toNode] > w) {
				dist[toNode] = w;
				pq.push({ w, toNode });
			}
		}
	}
	return;
}

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> V >> E;
	int st;
	cin >> st;
	int u, v, w;
	for (int i = 0; i < E; i++) {
		cin >> u >> v >> w;
		graph[u].push_back({ v,w });
	}

	dijst(st);

	for (int i = 1; i <= V; i++) {
		if (dist[i] == INF) {
			cout << "INF" << "\n";
		}
		else {
			cout << dist[i] << "\n";
		}
	}


	return 0;
}