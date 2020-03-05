#include "GitHelper.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    GitHelper w;
    w.show();
    return a.exec();
}
