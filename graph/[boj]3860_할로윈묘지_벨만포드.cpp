#include <iostream>
#include <utility>
#include <vector>

#define INF 987654321

using namespace std;

int dR[4] = { 0,0,-1,1 };
int dC[4] = { 1,-1,0,0 };

int main() {
	while (1) {
		int W, H;
		int G;
		int x, y;
		int E;
		int x1, y1, x2, y2, t;

		// dist[i] : i노드까지의 거리
		int dist[31 * 31];
		// { {a,b,c}, ...} : a->b 의 가중치 c
		vector<vector<int>> edge;
		// v[i][j] : i행 j열의 노드번호, (묘비는 노드번호가 -1)
		int	V[31][31];
		// 귀신구멍은1, 그냥노드는 0.
		int hole[31][31];

		cin >> W >> H;
		if (W == 0 && H == 0) {
			break;
		}
		//test case 시작
		else {
			// 배열 초기화
			for (int i = 0; i < H; i++) {
				for (int j = 0; j < W; j++) {
					V[i][j] = i * W + j;
					hole[i][j] = 0;
					dist[V[i][j]] = INF;
				}
			}


			// 묘비
			cin >> G;
			for (int i = 0; i < G; i++) {
				cin >> x >> y;
				V[y][x] = -1;
			}

			//귀신구멍
			cin >> E;
			for (int i = 0; i < E; i++) {
				cin >> x1 >> y1 >> x2 >> y2 >> t;
				hole[y1][x1] = 1;
				edge.push_back({ V[y1][x1],V[y2][x2],t });
			}

			//노드간 연결시작
			for (int i = 0; i < H; i++) {
				for (int j = 0; j < W; j++) {
					// 묘비이거나 귀신굴이면 continue
					if (V[i][j] == -1 || hole[i][j] == 1) {
						continue;
					}
					for (int k = 0; k < 4; k++) {
						int r = i + dR[k];
						int c = j + dC[k];
						if (r < 0 || r == H || c < 0 || c == W || V[r][c] == -1) {
							continue;
						}
						edge.push_back({ V[i][j],V[r][c],1 });
					}
				}
			}

			int s = edge.size();
			dist[0] = 0;
			bool isChanged = false;
			for (int i = 0; i < W*H - G; i++) {
				isChanged = false;

				for (int j = 0; j < s; j++) {
					int from = edge[j][0];
					int to = edge[j][1];
					int cost = edge[j][2];


					if (from == W * H - 1) {
						continue;
					}


					if (dist[from] != INF && dist[to] > dist[from] + cost) {
						isChanged = true;
						dist[to] = dist[from] + cost;
					}
				}
				if (!isChanged) {
					break;
				}
			}

			// 끝이 바뀌고 끝났으면 음의 순환 존재
			if (isChanged) {
				cout << "Never\n";
			}
			// 안바뀌었는데 끝까지 갔을때 경로 존재x
			else if (dist[H*W - 1] == INF) {
				cout << "Impossible\n";
			}
			else {
				cout << dist[H*W - 1] << "\n";
			}
		}


	}
}