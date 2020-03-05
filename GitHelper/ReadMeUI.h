#pragma once

#include <QDialog>
#include "ui_ReadMeUI.h"

class ReadMeUI : public QDialog
{
    Q_OBJECT

public:
    ReadMeUI(QWidget *parent = Q_NULLPTR);
    ~ReadMeUI();

private:
    Ui::ReadMeUI ui;
};
