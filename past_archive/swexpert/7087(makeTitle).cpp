#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int N;
		cin >> N;
		string word;
		vector<int> iniV{};
		int ans = 0;
		int target = 65;

		for (int j = 0; j < N; j++) {
			cin >> word;
			iniV.push_back(int(word[0]));
		}

		sort(iniV.begin(), iniV.end());

		for (int j = 0; j < iniV.size(); j++) {
			if (iniV[j] == target) {
				target++;
				ans++;
			}
			else if (iniV[j] == target - 1) {
				continue;
			}
			else {
				break;
			}
		}
		cout << "#" << i + 1 << " " << ans << endl;
	}
	
}