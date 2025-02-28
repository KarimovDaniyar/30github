#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private:
    Ui::MainWindow *ui;

private slots:
    void digits();
    void on_pushButton_dot_clicked();
    void operations();
    void on_pushButton_equals_clicked();
    void math();
    void on_pushButton_clear_clicked();
};
#endif // MAINWINDOW_H
