#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool isSame(char w1, char w2) {
	string s1 = "CEFGHIJKLMNSTUVWXYZ";
	string s2 = "ADOPQR";
	char s3 = 'B';

	if ((s1.find(w1) <= 18 and s1.find(w2) <= 18) or (s2.find(w1) <= 5 and s2.find(w2) <= 5) or (w1 == s3 and w2 == s3)) {
		return true;
	}
	else
		return false;
}

int main() {
	int t;
	string word1;
	string word2;
	cin >> t;

	for (int i = 0; i < t; i++) {
		bool w1samew2 = true;
		cin >> word1; cin >> word2;

		if (word1.size() != word2.size()) {
			cout << "#" << i + 1 << " DIFF" << endl;
			continue;
		}
		else {
			for (int j = 0; j < word1.size(); j++) {
				if (isSame(word1[j], word2[j]))
					continue;
				else {
					w1samew2 = false;
					break;
				}
			}
		}

		if (w1samew2 == true) {
			cout << "#" << i + 1 << " SAME" << endl;
		}
		else {
			cout << "#" << i + 1 << " DIFF" << endl;
		}
	}
}