#include<bits/stdc++.h>

using namespace std;

void zifu()

{

	int chang;

	cout << "输入字符数" << endl;

 cin>>chang;

system("clear");

	char zifu[45];

	for(int i=0;i<chang;i++)

	{

	cout << "输入字符" << endl;

 cin>>zifu[i];
system("clear");
	}

	cout << "加密结果是：";
	
for(int i=0;i<chang;i++)

	{

cout<<(int) (zifu[i])<<" ";

	}
cout << "\a" << endl;
}

void ascll()

{

	int chang2;

 cout << "输入数据数" << endl;

	cin>>chang2;//几个数据 

system("clear");

	int ascll[128];

	for(int i=0;i<chang2;i++)

	{

		cout << "输入数据" << endl;

 cin>>ascll[i];

system("clear");

	}

cout << "解密结果是:" << endl;

		for(int i=0;i<chang2;i++)

	{

		cout<<(char) (ascll[i]);

	}

cout << "\a" << endl;

}

int main()

{
	int c;

	cout << "0加1解" << endl;

 cin>>c;

 system("clear");

if(c==0) 

	{

	zifu();

	}

	if(c==1)

	{

	ascll();

	}

	return 0;

}