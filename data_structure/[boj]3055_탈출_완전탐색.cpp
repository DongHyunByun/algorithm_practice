#include <iostream>
#include <algorithm>

using namespace std;

char arr[50][50];

int dR[4] = { 0,0,-1,1 };
int dC[4] = { 1,-1,0,0 };
int R, C;

//차면 1
bool water[50][50];
bool go[50][50];

void waterSpread() {
	//물 퍼짐
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (water[i][j]) {
				int tempR, tempC;
				for (int k = 0; k < 4; k++) {
					tempR = i + dR[k];
					tempC = j + dC[k];
					// 범위벗어나지않고, 돌도아니고 비버의 굴도 아니면
					if (tempR >= 0 and tempR < R and tempC >= 0 and tempC < C and arr[tempR][tempC] != 'D' and arr[tempR][tempC] != 'X') {
						arr[tempR][tempC] = '*';
					}
				}
			}
		}
	}

	// 물채워진곳 1로 채움
	// 물 퍼지면서 water[i][j]를 채우면 한번에 끝까지 다차기 때문에 나눠서 생각.
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (arr[i][j] == '*') {
				water[i][j] = 1;
			}
		}
	}
}

bool move() {
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (go[i][j]) {
				int tempR, tempC;
				for (int k = 0; k < 4; k++) {
					tempR = i + dR[k];
					tempC = j + dC[k];
					if (tempR >= 0 and tempR < R and tempC >= 0 and tempC < C and arr[tempR][tempC] != 'X' and arr[tempR][tempC] != '*') {
						arr[tempR][tempC] = 'S';
					}
				}
			}
		}
	}

	// 고슴도치 움직임
	bool isNotMove = true;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			// 새로 움직인 자리
			if (arr[i][j] == 'S' and go[i][j]==0) {
				go[i][j] = 1;
				isNotMove = false;
			}
		}
	}
	if (isNotMove) {
		return false;
	}
	else {
		return true;
	}
}
int main() {
	cin >> R >> C;
	// 비버집 위치
	int locR, locC;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			cin >> arr[i][j];
			if (arr[i][j] == '*') {
				water[i][j] = 1;
			}
			else if (arr[i][j] == 'S') {
				go[i][j] = 1;
			}
			else if (arr[i][j] == 'D') {
				locR = i;
				locC = j;
			}
		}
	}
	int ans = 1;

	while (1) {
		waterSpread();
		if (move()) {
			if (go[locR][locC] == 1) {
				cout << ans << endl;
				break;
			}
		}
		else {
			cout << "KAKTUS" << endl;
			break;
		}
		ans++;
	}

	


	return 0;
}