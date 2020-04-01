#include "GitHelper.h"
#include <QtWidgets/QApplication>
//#include "Python.h"

int main(int argc, char *argv[])
{
    //Py_Initialize();
    //PyRun_SimpleString("print 'hello'");

    //Py_Finalize();    


    QApplication a(argc, argv);
    GitHelper w;
    w.show();
    return a.exec();
}
