#include <vector>
#include <queue>
#include <iostream>
using namespace std;


int bfs(vector<vector<int>> &V, int r, int c, int color, int m, int n) {
	int sizeOfArea = 1;
	int dR[] = { 0,0,-1,1 };
	int dC[] = { 1,-1,0,0 };

	V[r][c] = 0;
	queue<vector<int>> q;
	//cout << r << "¿Í" << c << endl;
	q.push({ r,c });

	while (!q.empty()) {
		vector<int> temp = q.front();
		q.pop();
		cout << temp[0] << " " << temp[1] << endl;
		for (int i = 0; i < 4; i++) {
			int tempR = temp[0] + dR[i];
			int tempC = temp[1] + dC[i];
			if (tempR >= 0 and tempC >= 0 and tempR < m and tempC < n and V[tempR][tempC] == color) {
				V[tempR][tempC] = 0;
				q.push({ tempR,tempC });
				sizeOfArea += 1;
			}
		}
	}
	//cout << "Á¾·á" << endl;
	return sizeOfArea;
}

vector<int> solution(int m, int n, vector<vector<int>> picture) {
	int number_of_area = 0;
	int max_size_of_one_area = 0;

	vector<int> answer(2);
	
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (picture[i][j] != 0) {
				number_of_area += 1;
				int area = bfs(picture, i, j, picture[i][j], m, n);
				if (area > max_size_of_one_area) {
					max_size_of_one_area = area;
				}
			}
		}
	}
	return { number_of_area,max_size_of_one_area };
}

int main() {
	vector<int> a=solution(6, 4, { {1,1,1,0},{1,2,2,0},{1,0,0,1},{0,0,0,1},{0,0,0,3},{0,0,0,3} });
	cout << a[0] << " " << a[1];
}