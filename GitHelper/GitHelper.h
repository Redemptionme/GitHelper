#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_GitHelper.h"

class GitHelper : public QMainWindow
{
    Q_OBJECT

public:
    GitHelper(QWidget *parent = Q_NULLPTR);
    void BindUI();

public slots:
    void ChooseDirClicked();
    void OpenDirClicked();
    void ReadMeClicked();

public:
    Ui::GitHelperClass ui;

    QString exePath;
    QString dirPath;
    QString branchName;
    QString gitPath;
};
