#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

// 부무노드 개수 저장
int parent[32001];

// togo[i]에는 i가 향하는 정점들을 저장
vector<int> togo[32001];

queue<int> q;

int main() {
	int N, M;
	cin >> N >> M;
	int A, B;

	for (int i = 0; i < M; i++) {
		cin >> A >> B;
		togo[A].push_back(B);
		parent[B]++;
	}
	
	for (int i = 1; i <= N; i++) {
		if (parent[i] == 0) {
			q.push(i);
		}
	}
	int temp;
	while (!q.empty()) {
		temp = q.front(); q.pop();
		cout << temp << " ";
		
		
		for (int i = 0; i < togo[temp].size(); i++) {
			// 부모하나줄이고
			parent[togo[temp][i]]--;
			if (parent[togo[temp][i]] == 0) {
				q.push(togo[temp][i]);
			}
		}
	}


	return 0;
}