#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool isCorrect(string ans, string myNum) {

	for (int i = 0; i < 8; i++) {
		if (ans[i] == '*' or ans[i]==myNum[i]) {
			continue;
		}
		else {
			return false;
		}
	}

	return true;
}

int main() {
	int t;
	int N, M;
	string ans;
	int money;
	string myNum;


	cin >> t;
	for (int i = 0; i < t;i++) {
		int ansMoney = 0;
		cin >> N >> M;
		vector<string> ansV{};
		vector<int> moneyV{};
		vector<string> myNumV{};

		for (int j = 0; j < N; j++) {
			cin >> ans >> money;
			ansV.push_back(ans);
			moneyV.push_back(money);
		}

		for (int k = 0; k < M; k++) {
			cin >> myNum;
			myNumV.push_back(myNum);
		}

		for (int l = 0; l < N;l++) {
			for (int m = 0; m < myNumV.size();m++) {
				if (isCorrect(ansV[l], myNumV[m])) {
					ansMoney += moneyV[l];

				}
			}
		}
		cout << "#" << i + 1 << " " << ansMoney << endl;
	}
}