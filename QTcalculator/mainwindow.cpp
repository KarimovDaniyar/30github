#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <qwindowdefs.h>


double first;


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    connect(ui->pushButton_0,SIGNAL(clicked()),this, SLOT(digits()));
    connect(ui->pushButton_1,SIGNAL(clicked()),this, SLOT(digits()));
    connect(ui->pushButton_2,SIGNAL(clicked()),this, SLOT(digits()));
    connect(ui->pushButton_3,SIGNAL(clicked()),this, SLOT(digits()));
    connect(ui->pushButton_4,SIGNAL(clicked()),this, SLOT(digits()));
    connect(ui->pushButton_5,SIGNAL(clicked()),this, SLOT(digits()));
    connect(ui->pushButton_6,SIGNAL(clicked()),this, SLOT(digits()));
    connect(ui->pushButton_7,SIGNAL(clicked()),this, SLOT(digits()));
    connect(ui->pushButton_8,SIGNAL(clicked()),this, SLOT(digits()));
    connect(ui->pushButton_9,SIGNAL(clicked()),this, SLOT(digits()));
    connect(ui->pushButton_plus_minus,SIGNAL(clicked()),this,SLOT(operations()));
    connect(ui->pushButton_procten,SIGNAL(clicked()),this,SLOT(operations()));
    connect(ui->pushButton_minus,SIGNAL(clicked()),this,SLOT(math()));
    connect(ui->pushButton_plus,SIGNAL(clicked()),this,SLOT(math()));
    connect(ui->pushButton_divide,SIGNAL(clicked()),this,SLOT(math()));
    connect(ui->pushButton_multip,SIGNAL(clicked()),this,SLOT(math()));

    ui->pushButton_multip->setCheckable(true);
    ui->pushButton_minus->setCheckable(true);
    ui->pushButton_plus->setCheckable(true);
    ui->pushButton_divide->setCheckable(true);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::digits()
{
    QPushButton *button = (QPushButton *)sender();

    double numbers;
    QString new_label;

    numbers = (ui->result_show->text()+button->text()).toDouble();
    new_label = QString::number(numbers,'g',15);

    ui->result_show->setText(new_label);
}

void MainWindow::on_pushButton_dot_clicked()
{
    if(!ui->result_show->text().contains("."))
        ui->result_show->setText(ui->result_show->text()+ ".");
}

void MainWindow::operations(){
    QPushButton *button = (QPushButton *)sender();
    double numbers;
    QString new_label;

    if(button->text() == "+/-"){
        numbers = (ui->result_show->text().toDouble());
        numbers *= -1;
        new_label = QString::number(numbers, 'g', 15);
        ui->result_show->setText(new_label);
    }

    else if(button->text() == "%"){
        numbers = (ui->result_show->text().toDouble());
        numbers *= 0.01;
        new_label = QString::number(numbers, 'g', 15);
        ui->result_show->setText(new_label);
    }
}

void MainWindow:: math()
{
    QPushButton *button = (QPushButton *)sender();
    first = ui->result_show->text().toDouble();
    ui->result_show->setText("");

    button->setChecked(true);

}

void MainWindow::on_pushButton_clicked()
{

}


void MainWindow::on_pushButton_equals_clicked()
{
    double labelNumber, second;
    QString new_label;

    second = ui->result_show->text().toDouble();


    if(ui->pushButton_plus->isChecked()){
        labelNumber = first+second;
        new_label = QString::number(labelNumber, 'g', 15);
        ui->result_show->setText(new_label);
        ui->pushButton_plus->setChecked(false);

    }else if(ui->pushButton_minus->isChecked()){
        labelNumber = first-second;
        new_label = QString::number(labelNumber, 'g', 15);
        ui->result_show->setText(new_label);
        ui->pushButton_minus->setChecked(false);

    }else if(ui->pushButton_divide->isChecked()){
        if(second == 0){
            ui->result_show->setText("0");
        }else{
            labelNumber = first/second;
            new_label = QString::number(labelNumber, 'g', 15);
            ui->result_show->setText(new_label);
            ui->pushButton_divide->setChecked(false);
        };

    }else if(ui->pushButton_multip->isChecked()){
        labelNumber = first*second;
        new_label = QString::number(labelNumber, 'g', 15);
        ui->result_show->setText(new_label);
        ui->pushButton_multip->setChecked(false);
    }
}
