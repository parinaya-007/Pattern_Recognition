#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int t, n;
    cin >> t;
    while(t--){
        cin >> n;
        long a[n];
        vector<bool> c(n+1, false);
        for(int i=0; i<n; i++){
            cin >> a[i];
        }
        bool check = true;
        for(int i=0; i<n; i++){
            c[a[i]] = true;
        }
        for(int i=1; i<=n; i++){
            if(c[i]==false)
                check = false;
        }
        int count = 0;
        for(int i=1; i<n; i++){
            if(a[i]>=a[i-1])
                count++;
        }
        if(count==n-1)
            check = false;
        if(check)
            cout << "Beautiful" << endl;
        else cout << "Ugly" << endl;
    }
    return 0;
}
