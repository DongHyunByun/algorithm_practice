#include <iostream>
#include <algorithm>

using namespace std;
int L[100000][3];
int maxL[3],minL[3],preMaxL[3],preMinL[3];

int main() {
	int N;
	cin >> N;
	
	for (int i = 0; i < N; i++) {
		cin >> L[i][0] >> L[i][1] >> L[i][2];
	}

	for (int j = 0; j < 3; j++) {
		preMinL[j] = L[0][j];
		preMaxL[j] = L[0][j];
	}

	for (int i = 1; i < N; i++) {
		//Ã¹¹øÂ°Ä­
		maxL[0] = L[i][0] + *max_element(preMaxL, preMaxL+2);
		minL[0] = L[i][0] + *min_element(preMinL, preMinL+2);

		//µÎ¹øÂ°Ä­
		maxL[1] = L[i][1] + *max_element(preMaxL, preMaxL+3);
		minL[1] = L[i][1] + *min_element(preMinL, preMinL+3);

		//¼¼¹øÂ°Ä­
		maxL[2] = L[i][2] + *max_element(preMaxL+1, preMaxL+3);
		minL[2] = L[i][2] + *min_element(preMinL+1, preMinL+3);

		for (int j = 0; j < 3; j++) {
			preMaxL[j] = maxL[j];
			preMinL[j] = minL[j];
		}
	
	}
	
	cout << *max_element(preMaxL, preMaxL + 3) << " " << *min_element(preMinL, preMinL + 3);

	return 0;
}