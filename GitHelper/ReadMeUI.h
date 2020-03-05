#pragma once

#include <QDialog>
#include "ui_ReadMeUI.h"
#include "GitHelper.h"

class ReadMeUI : public QDialog
{
    Q_OBJECT

public:
    ReadMeUI(QWidget *parent = Q_NULLPTR);
    ~ReadMeUI();
    void UpdateUI();
    void SetMainUI(GitHelper* pHelper);

private:
    Ui::ReadMeUI ui;
    GitHelper* pMainUI;
};
