#include <iostream>
#include <queue>
#include <map>
#include <set>

using namespace std;

map<int,set<int>> graph;
int visitedL[1001];

void dfs(int v) {
	cout << v << " ";
	visitedL[v] = 1;
	for (auto it = graph[v].begin(); it != graph[v].end(); it++) {
		if (!visitedL[*it]) {
			dfs(*it);
		}
	}
}

void bfs(int v) {
	queue<int> q;
	q.push(v);
	visitedL[v] = 1;
	int temp;
	while (!q.empty()) {
		temp = q.front(); q.pop();
		cout << temp << " ";
		for (auto it = graph[temp].begin(); it != graph[temp].end(); it++) {

			if (!visitedL[*it]) {
				q.push(*it);
				visitedL[*it] = 1;
			}
		}
	}
}

int main() {
	int N, M, V;
	cin >> N >> M >> V;
	int temp1, temp2;
	for (int i = 0; i < M; i++) {
		cin >> temp1 >> temp2;
		if (graph.find(temp1) == graph.end()) {
			graph[temp1] = { temp2 };
		}
		else {
			graph[temp1].insert(temp2);
		}

		if (graph.find(temp2) == graph.end()) {
			graph[temp2] = { temp1 };
		}
		else {
			graph[temp2].insert(temp1);
		}
	}

	dfs(V);
	for (int i = 0; i < 1001; i++) {
		visitedL[i] = 0;
	}
	cout << endl;
	bfs(V);

	return 0;
}
