#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

// �ι���� ���� ����
int parent[32001];

// togo[i]���� i�� ���ϴ� �������� ����
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
			// �θ��ϳ����̰�
			parent[togo[temp][i]]--;
			if (parent[togo[temp][i]] == 0) {
				q.push(togo[temp][i]);
			}
		}
	}


	return 0;
}