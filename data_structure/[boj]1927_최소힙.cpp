#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int N,num;
	priority_queue<int> pq;

	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> num;
		if (num != 0) {
			pq.push(-num);
		}
		else {
			if (!pq.empty()) {
				cout << -pq.top() << "\n";
				pq.pop();
			}
			else {
				cout << 0 << "\n";
			}
		}
	}
	pq.size()
	return 0;
}