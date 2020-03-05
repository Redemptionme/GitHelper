#include "ReadMeUI.h"

ReadMeUI::ReadMeUI(QWidget *parent)
    : QDialog(parent)
{
    ui.setupUi(this);
    this->UpdateUI();
}

ReadMeUI::~ReadMeUI()
{
}

void ReadMeUI::UpdateUI()
{

}

void ReadMeUI::SetMainUI(GitHelper* pHelper)
{
    pMainUI = pHelper;
}
