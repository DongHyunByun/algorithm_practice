#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;
int n, m, k;
// graph[i]={(j,w),(j,w)...} : i에서 j로의 가중치 w
vector<pair<int, int>> graph[1001];

// k번째숫자를 저장
int ans[1001] = { -1, };

// visit[i] : i에 방문한 횟수, k가 됐을 때 ans에 저장할것
int visit[1001];

int main() {
	cin >> n >> m >> k;
	int a, b, c;
	for (int i = 0; i < m; i++) {
		cin >> a >> b >> c;
		graph[a].push_back({ b,c });
	}
	
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	int count = 0; 
	int endCount = n * k;
	pq.push({ 0,1 });
	while (!pq.empty()) {
		int cost = pq.top().first;
		int nowNode = pq.top().second;
		pq.pop();

		if (visit[nowNode] >= k) {
			continue;
		}
		visit[nowNode] += 1;
		if (visit[nowNode] == k) {
			ans[nowNode] = visit[nowNode];
		}
		
	}


	return 0;
}