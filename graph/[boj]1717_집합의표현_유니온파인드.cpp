#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int parent[1000001];


int find(int x) {
	if (parent[x] == x) {
		return x;
	}
	else {
		return parent[x] = find(parent[x]);
	}
}

void uni(int x, int y) {
	x = find(x);
	y = find(y);
	
	parent[x] = y;
}

int main() {
	cin.tie(0);
	cout.tie(0);
	int n, m;
	int op, a, b;

	cin >> n >> m;
	for (int i = 0; i < n+1; i++) {
		parent[i] = i;
	}

	for (int i = 0; i < m; i++) {
		cin >> op >> a >> b;
		if (op == 1) {
			if (find(a) == find(b)) {
				cout << "YES\n";
			}
			else {
				cout << "NO\n";
			}
		}
		else {
			uni(a, b);
		}
	}

	return 0;
}
