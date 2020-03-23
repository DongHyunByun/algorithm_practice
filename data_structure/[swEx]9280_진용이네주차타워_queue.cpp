#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;
int N[100];
int M[2000];

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int n, m;
		int visited[100];
		for (int i = 0; i < 100; i++) {
			visited[i] = -1;
		}
		cin >> n >> m;
		for (int i = 0; i < n; i++) {
			cin >> N[i];
		}
		for (int i = 0; i < m; i++) {
			cin >> M[i];
		}
		int car;
		int park = 0;
		queue<int> q;
		int ans = 0;
		for (int i = 0; i < 2 * m; i++) {
			cin >> car;
			if (car > 0) {
				car--;
				if (park == n) {
					q.push(car);
					continue;
				}
				else {
					for (int area = 0; area < n; area++) {
						if (visited[area] == -1) {
							visited[area] = car;
							park++;
							ans += N[area] * M[car];
							break;
						}
					}
				}
			}
			else {
				car++;
				car = -1 * car;
				if (!q.empty()) {
					for (int j = 0; j < n; j++) {
						if (visited[j] == car) {
							int qNum = q.front(); q.pop();
							visited[j] = qNum;
							ans += N[j] * M[qNum];
							break;
						}
					}
				}
				else {
					for (int j = 0; j < n; j++) {
						if (visited[j] == car) {
							visited[j] = -1;
							park--;
							break;
						}
					}
				}
			}
		}
		cout << "#" << t + 1 << " " << ans << endl;
	}


	return 0;
}