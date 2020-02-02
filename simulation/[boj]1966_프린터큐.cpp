#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		vector<int> vec;
		int N, M;
		int inputNum;
		int ans = 1;
		cin >> N >> M;

		for (int j = 0; j < N; j++) {
			cin >> inputNum;
			vec.push_back(inputNum);
		}

		int temp;
		bool isErase;
		while (1) {
			temp = vec[0];
			vec.erase(vec.begin());
			isErase = true;
			for (int j = 0; j < vec.size(); j++) {
				if (temp < vec[j]) {
					isErase = false;
					break;
				}
			}
			if (isErase) {
				if (M == 0) {
					cout << ans<<endl;
					break;
				}
				else {
					M--;
					ans++;
				}
			}
			else {
				if (M == 0) {
					vec.push_back(temp);
					M = vec.size()-1;
					
				}
				else {
					M--;
					vec.push_back(temp);
				}
			}
		}
	}
}