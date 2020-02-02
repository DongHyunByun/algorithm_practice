#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
char pass[15];
char mom[5] = { 'a','e','i','o','u' };
int L, C;
vector<string> ans;

void dfs(int m, int s, int loc, vector<char> nowWord) {
	if (nowWord.size()==L) {
		if (m >= 1 and s>=2) {
			string st = "";
			sort(nowWord.begin(), nowWord.end());
			for (int i = 0; i < L; i++) {
				st += nowWord[i];
			}
			ans.push_back(st);
		}
		return;
	}
	if (loc == C) {
		return;
	}

	char temp = pass[loc];
	// loc위치의 단어를 더하는경우
	nowWord.push_back(temp);
	if (find(begin(mom), end(mom), temp) != end(mom)) {
		dfs(m + 1, s, loc + 1, nowWord); //모음일때
	}
	else {
		dfs(m, s + 1, loc + 1, nowWord); //자음일때
	}

	// loc위치의 단어를 더하지 않는 경우
	nowWord.pop_back();
	dfs(m, s, loc + 1, nowWord);
}
int main() {
	cin >> L;
	cin >> C;
	for (int i = 0; i < C; i++) {
		cin >> pass[i];
	}
	vector<char> ini;

	dfs(0, 0, 0, ini);
	sort(ans.begin(), ans.end());
	for (int i = 0; i < ans.size(); i++) {
		cout << ans[i] << endl;
	}
	return 0;
}