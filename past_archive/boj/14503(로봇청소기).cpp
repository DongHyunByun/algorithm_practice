#include <iostream>
using namespace std;

#define maxSize 51

int main() {
	int ans = 1;
	int N, M, r, c, d;
	cin >> N >> M;
	cin >> r >> c >> d;
	int L[maxSize][maxSize];
	int dr[4][4] = { {0,1,0,-1},{-1,0,1,0},{0,-1,0,1},{1,0,-1,0} };
	int dc[4][4] = { {-1,0,1,0},{0,-1,0,1},{1,0,-1,0},{0,1,0,-1} };

	int backR[4] = { 1,0,-1,0 };
	int backC[4] = { 0,-1,0,1 };

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> L[i][j];
		}
	}
	L[r][c] = 3;

	while (1) {
		/*
		cout << r << c << d << endl;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				cout << L[i][j] << " ";
			}
			cout << endl;
		}
		*/

		bool isClean = false;
		for (int i = 0; i < 4; i++) {
			int tempR = r + dr[d][i];
			int tempC = c + dc[d][i];
			int tempD = d - (i + 1);

			if (tempD < 0) {
				tempD += 4;
			}

			if (L[tempR][tempC] == 0) {
				isClean = true;
				ans += 1;
				L[tempR][tempC] = 3;
				r = tempR;
				c = tempC;
				d = tempD;
				break;
			}
		}
		if (!isClean) {
			r = r + backR[d];
			c = c + backC[d];
			if (L[r][c] == 1) {
				break;
			}
		}
		

	}
	cout << ans;
	return 0;
}