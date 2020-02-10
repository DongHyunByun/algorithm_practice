#include <iostream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

string s[50];
vector<int> antic = { 0, 2, 8, 13, 19 };
int N, K;
int ans = 0;

void learn(vector<int> al, int toLearn, int nowIndx) {

	//cout << "인덱스 : " << nowIndx << " 남은 배움수 : " << toLearn << endl;
	if (toLearn == 0) {
		//확인용 출력
		/*
		for (int i = 0; i < 26; i++) {
			cout << al[i] << " ";
		}
		cout << endl;
		*/

		int cnt = 0;
		//단어들 검사시작
		for (int i = 0; i < N; i++) {
			int wordLen = s[i].size();
			bool isPossible = true;
			for (int j = 0; j < wordLen; j++) {
				//안배운 음절이면 바로 종료
				if (al[s[i][j] - 'a'] == 0) {
					isPossible = false;
					break;
				}
			}
			if (isPossible) {
				cnt++;
			}
		}
		if (cnt > ans) {
			ans = cnt;
		}
		return;
	}
	// 못배우고 마지막까지 오면 종료
	if (nowIndx == 26) {
		return;
	}

	//antic이면 다음재귀
	if (find(antic.begin(), antic.end(), nowIndx) != antic.end()) {
		learn(al, toLearn, nowIndx + 1);
		return;
	}

	//nowIndx 학습x
	learn(al, toLearn, nowIndx + 1);
	//nowIndx 학습o
	al[nowIndx] = 1;
	learn(al, toLearn - 1, nowIndx + 1);
}


int main() {
	vector<int> alpa(26);
	cin >> N >> K;
	for (int i = 0; i < N; i++) {
		cin >> s[i];
	}
	// 이건무조건 다배워야함
	for (int i = 0; i < 5; i++) {
		alpa[antic[i]] = 1;
	}

	int toLearn = (K - 5);

	if (toLearn < 0) {
		ans = 0;
	}
	else {
		learn(alpa, toLearn, 0);
	}

	cout << ans;

	return 0;
}