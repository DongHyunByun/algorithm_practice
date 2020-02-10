#include <iostream>
#include <algorithm>

using namespace std;

int tree[1000000];
int N, M;

//���̰������� 0, ���ڸ��� 1, ������ 2
int cut(int loc) {
	int getTree = 0;
	for (int i = 0; i < N; i++) {
		if (tree[i] > loc) {
			getTree += tree[i] - loc;
		}
	}
	if (getTree > M) {
		return 0;
	}
	else if (getTree<M) {
		return 1;
	}
	else {
		return 2;
	}
}

int binarySearch(int down, int up) {
	int temp;
	while (down <= up) {
		temp = cut(mid);
		int mid = (down + up) / 2;
		// ���̰�������
		if (temp==0) {
			up = mid - 1;
		}
		//���԰�������
		else if (temp==1) {
			down = mid + 1;
		}
		else {
			return mid;
		}
		cout << mid << endl;
	}
}

int main() {
	cin >> N, M;
	for (int i = 0; i < N; i++) {
		cin >> tree[i];
	}
	cout << *max_element(tree, tree + N) << endl;
	//cout << binarySearch(0, *max_element(tree, tree + N));
	return 0;
}