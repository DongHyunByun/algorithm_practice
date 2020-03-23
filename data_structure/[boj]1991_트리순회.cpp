#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <vector>

using namespace std;

vector<vector<char>> vec;
int N;


void preorder(char c) {
	for (int i = 0; i < N; i++) {
		if (vec[i][0] == c) {
			cout << c;
			preorder(vec[i][1]);
			preorder(vec[i][2]);
			break;
		}
	}
	return;
}

void inorder(char c) {
	for (int i = 0; i < N; i++) {
		if (vec[i][0] == c) {
			inorder(vec[i][1]);
			cout << c;
			inorder(vec[i][2]);
			break;
		}
	}
	return;
}

void postorder(char c) {
	for (int i = 0; i < N; i++) {
		if (vec[i][0] == c) {
			postorder(vec[i][1]);
			postorder(vec[i][2]);
			cout << c;
			break;
		}
	}
	return;
}

int main() {	
	cin >> N;
	char c1, c2, c3;
	for (int i = 0; i < N; i++) {
		cin >> c1 >> c2 >> c3;
		vec.push_back({ c1,c2,c3 });
	}
	preorder('A');
	cout << endl;

	inorder('A');
	cout << endl;

	postorder('A');
	cout << endl;
	return 0;
}