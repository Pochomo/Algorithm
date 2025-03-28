#include <iostream>
using namespace std;

int dx[4] = {0, 1, 0, -1}, dy[4] = {1, 0, -1, 0};
int arrA[100][100] = {0};

bool InRange(int x, int y, int n, int m) {
    return (0 <= x && x < n && 0 <= y && y < m);
}

int main() {
    int n, m;
    cin >> n >> m;
    arrA[0][0] = 1;
    int direction = 0;
    int x = 0, y = 0;
    int nx = 0, ny = 0;
    for(int i = 1; i < n * m; i++){
        nx = x + dx[direction], ny = y + dy[direction];
        if(!InRange(nx, ny, n, m) || arrA[nx][ny] != 0){
            direction = (direction + 1) % 4;
        }
        x = x + dx[direction];
        y = y + dy[direction];
        arrA[x][y] = i + 1;
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << arrA[i][j] << " ";
        }
        cout << endl;
    }



    return 0;
}