// Day1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    ifstream myfile("data.txt");
    string mystring;
    vector<int> depth;
    vector<int> d3;
    while (myfile.eof() == false) {
        int next;
        myfile >> next;
        depth.push_back(next);
    }
    myfile.close();
    int inc=0;
    for (int i = 1; i < depth.size(); i++) {
        if (depth[i] > depth[i -1]) {
            inc++;
        }
    }
    cout << "Part 1: "<<inc << endl;
   
    int start = 0;
    for (int i = 0; i < depth.size(); i++) {
        int letter = 0;
        for (int j = 0; j < 3; j++) {
            if ((i+j) < depth.size()) {
                letter = letter + depth[i + j];
            }
        }
        d3.push_back(letter);
        start++;
    }

    inc = 0;
    for (int i = 1; i < d3.size(); i++) {
        if (d3[i] > d3[i - 1]) {
            inc++;
        }
    }
    cout << "Part 2: " << inc << endl;

    return 0;
}

