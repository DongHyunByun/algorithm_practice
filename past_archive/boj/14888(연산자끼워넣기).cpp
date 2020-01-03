#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int calculate(int A, int cal, int B) {
	if (cal == 0) {
		return A + B;
	}
	else if (cal == 1) {
		return A - B;
	}
	else if (cal == 2) {
		return A * B;
	}
	else {
		return A/B;
	}
}

int main() {
	int max = -1000000000;
	int min = 1000000000;
	int n;
	cin >> n;
	vector<int> num(n);
	vector<int> toPermu;
	vector<int> temp;
	// (+,-,*,//)
	int cal[] = { 0, 0, 0, 0 };
	for (int i = 0; i < n; i++) {
		cin >> num[i];
	}
	for (int i = 0; i < 4; i++) {
		cin >> cal[i];
	}
	for (int i = 0; i < 4; i++) {
		int t = cal[i];
		for (int j = 0; j < t; j++) {
			toPermu.push_back(i);
		}
	}
	/*
	printf("topermu");
	for (auto a : toPermu) {
		printf("%d ", a);
	}
	printf("\n");
	*/

	do {
		temp.clear();
		for (int i = 0; i < toPermu.size(); i++) {
			temp.push_back(toPermu[i]);
		}

		/*
		for (auto a : temp) {
			printf("%d ",a);
		}
		printf("\n");
		*/

		int tempAns = num[0];
		for (int i = 0; i < n - 1; i++) {
			tempAns = calculate(tempAns, temp[i], num[i + 1]);
		}
		if (tempAns < min){
			min = tempAns;
		}
		if (tempAns > max) {
			max = tempAns;
		}
		//printf("%d", tempAns);
	} while (next_permutation(toPermu.begin(), toPermu.end()));
	
	printf("%d\n", max);
	printf("%d", min);

	return 0;
}