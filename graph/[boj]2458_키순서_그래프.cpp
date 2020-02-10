#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

vector<int> to[501];
vector<int> reversedTo[501];


int main() {
	int ans = 0;
	int N, M;
	cin >> N >> M;

	int a, b;
	for (int i = 0; i < M; i++) {
		cin >> a >> b;
		to[a].push_back(b);
		reversedTo[b].push_back(a);
	}

	// 각 학생별로 bfs돈다
	for (int i = 1; i <= N; i++) {
		int cheakedL[501] = { 0, };
		int temp;
		queue<int> q;

		//앞으로 탐색
		int taller = 0;
		q.push(i);
		cheakedL[i] = 1;
		while (!q.empty()) {
			temp = q.front(); q.pop();
			for (int j = 0; j < to[temp].size(); j++) {
				if (cheakedL[to[temp][j]] != 1) {
					q.push(to[temp][j]);
					cheakedL[to[temp][j]] = 1;
					taller += 1;
				}
			}
		}

		//뒤로 탐색
		int shorter = 0;
		q.push(i);
		while (!q.empty()){
			temp = q.front(); q.pop();
			for (int j = 0; j < reversedTo[temp].size(); j++) {
				if (cheakedL[reversedTo[temp][j]] != 1) {
					q.push(reversedTo[temp][j]);
					cheakedL[reversedTo[temp][j]]=1;
					shorter += 1;
				}
			}
 		}
		if (taller + shorter == N - 1) {
			ans += 1;
		}
	}
	cout << ans;

	return 0;
}