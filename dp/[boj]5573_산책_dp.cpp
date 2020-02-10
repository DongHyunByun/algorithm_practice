#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int d[1002][1002];
int map[1002][1002];

int main() {	
	int H, W, N;
	cin >> H >> W >> N;
	
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= W; j++) {
			cin >> map[i][j];
		}
	}

	// n-1산책 후 상태를 만든다.
	d[1][1] = N-1;
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= W; j++) {
			/*
			if (d[i][j] == 0) {
				continue;
			}
			*/

			d[i + 1][j] += d[i][j] / 2;
			d[i][j + 1] += d[i][j] / 2;

			if (d[i][j]%2==1) {
				if (map[i][j] == 1) {
					d[i][j + 1]++;
				}
				else {
					d[i + 1][j]++;
				}
			}
			map[i][j] = (map[i][j] + d[i][j]) % 2;
		}
	}

	//N번째 산책 시작
	int r = 1;
	int c = 1;
	while (1) {
		if (map[r][c] == 1) {
			c++;
		}
		else {
			r++;
		}
		if (c == W + 1 or r == H + 1) {
			break;
		}
	}
	cout << r << " " << c;
	
	
	
	return 0;
}