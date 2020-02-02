#include <iostream>
#include <vector>
#include <queue>

using namespace std;
vector<vector<int>> home;
//최소거리를 찾을때 queue로 bfs구현했을때 오류가 메모리 초과가 뜸

vector<vector<int>> chic;
int N, M, temp;
int dR[4] = {-1,1,0,0};
int dC[4] = {0,0,-1,1};
int finalAns=99999999;

int chicDist(int m[][50]) {
	int ans = 0;
	//각집마다 치킨거리를 구한다
	for (int i = 0; i < home.size(); i++) {
		pair<int, int> temp;
		int cheak[50][50] = { 0, };
		int r = home[i][0];
		int c = home[i][1];
		bool isfind;
		queue<pair<int,int>> q;
		q.push(make_pair(r,c));
		while (1) {
			isfind = false;
			int movedR,movedC;
			temp = q.front();
			q.pop();
			r = temp.first;
			c = temp.second;
			for (int k = 0; k < 4; k++) {
				movedR = r + dR[k];
				movedC = c + dC[k];
				if (movedR >= 0 and movedR < 50 and movedC >= 0 and movedC < 50) {
					if (m[movedR][movedC] == 2) {
						ans += (cheak[r][c] + 1);
						isfind = true;
					}
					else {
						q.push({ movedR,movedC });
						cheak[movedR][movedC] = cheak[r][c] + 1;
					}
				}
			}
			if (isfind) {
				break;
			}
		}
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
	m[r][c] = 0;
	dfs(m, loc + 1, erased - 1);

	//패점하지않을때
	m[r][c] = 2;
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