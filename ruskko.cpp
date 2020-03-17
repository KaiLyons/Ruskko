#include <iostream>
#include <string>
using namespace std;
string ext = ".rsko";
string output_args = "";

/*
###########################################
    Output
###########################################
*/

void outputProccess(){
    NULL;
}

/*
###########################################
    Syntax Lex/Parse
###########################################
*/

void lexparse(){
    NULL;
}


/*
###########################################
    Main File Functionality
###########################################
*/
// Filename Check
bool fileExtArg(string const &fname){
    if(fname.length() > ext.length()){
        return (0 == fname.compare(fname.length() - ext.length(), ext.length(), ext));
    } else {
        return false;
    }
}

// Main
int main(int argc, char *argv[]){
    cout << "Found " << argc - 1 << " total arguments" << endl;
    
    // Print all arguments
    for (int i = 1; i < argc; ++i){
        cout << "Argument Found: " << argv[i] << endl;
    }

    // Check file type
    if(!fileExtArg(argv[1])){
        cout << "============" << endl <<
        "Error 23: Wrong filename" << endl <<
        "Expected a \".rsko\" file!" << endl <<
        "Got \"" << argv[1] << "\" instead!!" << endl
        << "============" << endl;
    }

    // -o Options
    if (!(argv[2] == "-o")){
        cout << "Usage: ruskko [ruskko file] -o [html file]" << endl
        << "Example: ruskko index.rsko -o somepage.html" << endl;
        cout << "-o output args" << endl;
        cout << output_args << endl;
        if(argv[3] == NULL){
            cout << "Error 35:" << endl <<
            "the -o option is used but is never specified" << endl;
            return 1;
        }
        output_args = argv[3];
        cout << "Will output to:" << output_args << endl;
    }
}
