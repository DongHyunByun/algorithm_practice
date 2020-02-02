#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;
int L[26];
int main() {
	
	int N;
	string word;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> word;
		int charNum;
		int indx;
		int power = 0;
		for (int j = word.size() - 1; j >= 0; j--) {
			charNum = word[j];
			indx = charNum - 'A';
			L[indx] += pow(10, power);
			power++;
		}
	}
	sort(L,L+26, greater<int>());
	int ans = 0;
	for (int i = 0; i <10; i++) {
		ans += (L[i] * (9-i));
	}
	cout << ans;
}