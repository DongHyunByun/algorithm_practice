#include <iostream>
#include <algorithm>

using namespace std;

char arr[50][50];

int dR[4] = { 0,0,-1,1 };
int dC[4] = { 1,-1,0,0 };
int R, C;

//���� 1
bool water[50][50];
bool go[50][50];

void waterSpread() {
	//�� ����
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (water[i][j]) {
				int tempR, tempC;
				for (int k = 0; k < 4; k++) {
					tempR = i + dR[k];
					tempC = j + dC[k];
					// ����������ʰ�, �����ƴϰ� ����� ���� �ƴϸ�
					if (tempR >= 0 and tempR < R and tempC >= 0 and tempC < C and arr[tempR][tempC] != 'D' and arr[tempR][tempC] != 'X') {
						arr[tempR][tempC] = '*';
					}
				}
			}
		}
	}

	// ��ä������ 1�� ä��
	// �� �����鼭 water[i][j]�� ä��� �ѹ��� ������ ������ ������ ������ ����.
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

	// ����ġ ������
	bool isNotMove = true;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			// ���� ������ �ڸ�
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
	// ����� ��ġ
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