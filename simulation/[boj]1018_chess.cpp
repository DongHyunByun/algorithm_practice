#include <iostream>
#include <vector>
#include <string>

using namespace std;
string L[52];
string whiteFirst[8] = {
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
};

int main() {
	int N, M;
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> L[i];
	}
    int ans = 32;
    int com;
    //8*8판 짜르기 시작점 i,j
    for (int i = 0; i <= N - 8; i++) {
        for (int j = 0; j <= M - 8; j++) {
            //비교시작
            com = 0;
            for (int r = i; r < i + 8; r++) {
                for (int c = j; c < j + 8; c++) {
                    if (whiteFirst[r-i][c-j] != L[r][c]) {
                        com++;
                    }
                }
            }
            if (com > 32) {
                com = 64 - com;
            }
            if (ans > com) {
                ans = com;
            }
        }
    }
    cout << ans;
	return 0;
}