#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

int N, M, temp;
set<int> s;

int main() 
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N;
	for (int i = 0; i < N; ++i) {
		cin >> temp;
		s.insert(temp);
	}
	cin >> M;
	for (int i = 0; i < M; ++i) {
		cin >> temp;
		cout << (s.find(temp) == s.end() ? 0 : 1) << '\n';
	}
	return 0;
}