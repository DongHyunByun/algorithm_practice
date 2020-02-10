#include <iostream>
#include <algorithm>

using namespace std;

int rock[50];

int main() {
	int N = 0, M, K;
	double ans=0;

	//입력
	cin >> M;
	for (int i = 0; i < M; i++) {
		cin >> rock[i];
		N += rock[i];
	}
	cin >> K;

	double color, total, colorSum;
	//각 색깔의 돌을 뽑을 확률
	for (int i = 0; i < M; i++) {
		color = rock[i];
		total = N;
		colorSum = 1.0;
		for (int t = 0; t < K; t++) {
			colorSum *= (color / total);
			color--;
			total--;
			
		}
		ans += colorSum;
	}
	printf("%.15f", ans);
	return 0;
}