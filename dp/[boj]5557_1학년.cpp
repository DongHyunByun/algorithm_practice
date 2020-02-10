#include <iostream>
#include <algorithm>

using namespace std;

long long arr[21][101];

int main() {
	int N,temp;
	int add, sub;
	cin >> N;
	for (int j = 1; j <= N; j++) {
		cin >> temp;

		/*
		for (int r = 0; r < 21; r++) {
			for (int c = 0; c < 21; c++) {
				cout << arr[r][c] << " ";
			}
			cout << endl;
		}
		cout << endl;
		*/
		

		// Ã¹¹øÂ° °ª?
		if (j == 1) {
			arr[temp][j] = 1;
		}
		// ¸¶Áö¸· °ª?
		else if (j == N) {
			cout << arr[temp][j-1];
		}
		else {
			for (int i = 0; i <= 20; i++) {
				if (arr[i][j-1] != 0) {
					// µ¡¼À?
					add = i + temp;
					if (add >= 0 and add <= 20) {
						arr[add][j] += arr[i][j - 1];
					}
					// »¬¼À?
					sub = i - temp;
					if (sub >= 0 and sub <= 20) {
						arr[sub][j] += arr[i][j - 1];
					}
				}
			}
		}
	}


	return 0;
}