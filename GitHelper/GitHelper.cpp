#include "GitHelper.h"
#include <QtCore>
#include <QFileDialog>
#include <QDesktopServices>
#include "ReadMeUI.h"
//#include <CMsgIgnoreDialog>

GitHelper::GitHelper(QWidget *parent)
    : QMainWindow(parent)
{
    ui.setupUi(this);
    this->BindUI();
}

void GitHelper::BindUI()
{
    exePath = QDir::currentPath();

    QObject::connect(ui.ChooseDirBtn, SIGNAL(clicked()), this, SLOT(ChooseDirClicked()));
    QObject::connect(ui.OpenDirBtn, SIGNAL(clicked()), this, SLOT(OpenDirClicked()));    
    QObject::connect(ui.actionReadMe, &QAction::triggered, this, &GitHelper::ReadMeClicked);
}

void GitHelper::ReadMeClicked() 
{
    ReadMeUI* pDlg = new ReadMeUI;
    int ret = pDlg->exec();
    if (ret == QDialog::Accepted) {

    }
    delete pDlg;
}


void GitHelper::ChooseDirClicked()
{   
    QFileDialog* fileDialog = new QFileDialog(this);
    fileDialog->setWindowTitle(tr("Ñ¡ÔñProtoRootPath"));
    fileDialog->setFileMode(QFileDialog::Directory);
    fileDialog->setViewMode(QFileDialog::Detail); 
    if (fileDialog->exec()) {
        dirPath = fileDialog->directory().path();
    }
    ui.ChooseDirText->setText(dirPath);


}


void GitHelper::OpenDirClicked()
{
    if (dirPath.isEmpty()) {
        return;
    }
    QDesktopServices::openUrl(QUrl(dirPath, QUrl::TolerantMode));
}
