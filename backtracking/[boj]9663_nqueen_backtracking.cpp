#include <iostream>
#include <vector>

using namespace std;
int N;
int ans=0;

void dfs(vector<int> v,int s) {
	if (s == N) {
		ans++;
		return;
	}
	bool isPossible;
	for (int j = 0; j < N; j++) {
		isPossible = true;
		for (int col = 0; col < s; col++) {
			if ( j == v[col] or (s - col) == abs(j - v[col])) {
				isPossible = false;
				break;
			}
		}
		if (isPossible) {
			v[s] = j;
			dfs(v, s + 1);
		}
	}
}

int main() {
	cin >> N;
	vector<int> vec(15);
	for (int i = 0; i < N; i++) {
		vec[0] = i;
		dfs(vec,1);
	}
	cout << ans;


	return 0;
}