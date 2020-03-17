#include <iostream>
#include <string>
using namespace std;

bool fileExtArg(string const &fname){
    string ext = ".rsko";

    if(fname.length() > ext.length()){
        return (0 == fname.compare(fname.length() - ext.length(), ext.length(), ext));
    } else {
        return false;
    }
}

int main(int argc, char *argv[]){
    cout << "Found " << argc - 1 << " total arguments" << endl;
    
    for (int i = 1; i < argc; ++i){
        cout << "Argument Found: " << argv[i] << endl;
    }

    if(!fileExtArg(argv[1])){
        cout << "============" << endl <<
        "Error 23: Wrong filename" << endl <<
        "Expected a \".rsko\" file!" << endl <<
        "Got a \"" << argv[1] << "\" instead!!" << endl
        << "============" << endl;
    }
}
