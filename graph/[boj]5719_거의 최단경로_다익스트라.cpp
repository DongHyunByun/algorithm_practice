#include <iostream>
#include <utility>
#include <vector>
#include <queue>
#include <functional>

#define INF 987654321

using namespace std;
int N, M, S, D;

// dist[i][j] : i���� j���� �ִܰŸ� (i�� j�� ������ ���)
long long dist[500][500];

// dist2[i] : s���� i �������� �ִܰŸ�
long long dist2[500];

void dijs() {
	for (int i = 0; i < N; i++) {
		dist2[i] = INF;
	}
	dist2[S] = 0;
	// { {�ִܰŸ�,���} }
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
		// test case ����
		else {
			// ������ ����
			cin >> S >> D;

			// edge �ʱ�ȭ �� ä���
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

			// �ִܰŸ� ã��
			dijs();

			// ���������� ������ Ž���ϸ� �ִܰŸ� �����
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
					// �ִܰ���� �ϳ�
					if (dist2[nowNode] == dist[i][nowNode] + dist2[i]) {
						dist[i][nowNode] = INF;
						q.push(i);
					}
				}
			}

			// �ִܰŸ��� �����ϰ� �ִܰŸ�ã��
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