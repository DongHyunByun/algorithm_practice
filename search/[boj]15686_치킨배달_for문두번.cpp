#include <iostream>
#include <vector>
#include <queue>

using namespace std;
vector<vector<int>> home;
vector<vector<int>> chic;
//닫으면 1
bool closedChic[13];
int N, M, temp;
int finalAns = 99999999;

int chicDist(int m[][50]) {
	int ans = 0;
	//각집마다 치킨거리를 구한다
	for (int i = 0; i < home.size(); i++) {
		int minLen = 99999999;
		for (int j = 0; j < chic.size(); j++) {
			if (!closedChic[j]) {
				int temp = abs(home[i][0] - chic[j][0]) + abs(home[i][1] - chic[j][1]);
				if (minLen > temp) {
					minLen = temp;
				}
			}
		}
		ans += minLen;
	}
	return ans;
}


void dfs(int m[][50], int loc, int erased) {
	if (erased == 0) {
		int temp = chicDist(m);
		
		if (finalAns > temp) {
			finalAns = temp;
		}
		return;
	}
	if (loc == chic.size()) {
		return;
	}

	int r = chic[loc][0];
	int c = chic[loc][1];

	//loc번째 치킨집 패점할때
	closedChic[loc] = true;
	dfs(m, loc + 1, erased - 1);

	//패점하지않을때
	closedChic[loc] = false;
	dfs(m, loc + 1, erased);
}

int main() {
	int map[50][50];
	int toerase;
	int N, M, temp;
	cin >> N;
	cin >> M;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> temp;
			if (temp == 1) {
				home.push_back({ i,j });
			}
			else if (temp == 2) {
				chic.push_back({ i,j });
			}
			map[i][j] = temp;
		}
	}
	toerase = chic.size() - M;

	dfs(map, 0, toerase);

	cout << finalAns;
}