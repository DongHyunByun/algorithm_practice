#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

int main() {
	int num1, num2;
	string ans;
	int t = 1;
	while (1) {
		cin >> num1 >> num2;
		if (num1 < 0) {
			break;
		}
		// test case
		else {
			vector<pair<int, int>> graph;
			set<int> s;
			// ют╥б
			while (1) {
				if (num1 == 0 and num2 == 0) {
					break;
				}
				else {
					graph.push_back(make_pair(num1, num2));
					s.insert(num1);
					s.insert(num2);
				}
				cin >> num1 >> num2;
			}
			if (s.size() - 1 == graph.size() or s.size()==0) {
				printf("Case %d is a tree.\n", t);
			}
			else {
				printf("Case %d is not a tree.\n", t);
			}
		}
		t++;
	}

	return 0;
}
