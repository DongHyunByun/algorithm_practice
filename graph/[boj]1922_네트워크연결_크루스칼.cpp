#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

int parent[1001];

int find(int x) {
	if (x == parent[x]) {
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

bool cmp(vector<int> v1, vector<int> v2) {
	if (v1[2] < v2[2]) {
		return true;
	}
	else {
		return false;
	}
	//return v1[2] < v2[2];
}

int main() {
	vector<vector<int>> node;
	int n,m;
	cin >> n >> m;
	stack<int> s;

	int a, b, c;
	for (int i = 0; i < m; i++) {
		cin >> a >> b >> c;
		node.push_back({ a,b,c });
	}

	for (int i = 1; i <= n; i++) {
		parent[i] = i;
	}
	
	sort(node.begin(), node.end(), cmp);

	int temp1, temp2, cnt=0, ans=0;
	for (int i = 0; i < node.size(); i++) {
		temp1 = find(node[i][0]);
		temp2 = find(node[i][1]);
		// 루트노드가 다르다면 (연결해도 사이클이 생기지 않는다면)
		if (temp1 != temp2) {
			uni(temp1, temp2);
			cnt++;
			ans += node[i][2];
			// 노드개수-1 = 간선개수
			if (cnt == n - 1) {
				break;
			}
		}
	}
	cout << ans;

	return 0;
}