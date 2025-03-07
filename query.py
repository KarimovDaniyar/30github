"""
CREATE TABLE users(
    id BIGINT NOT NULL PRIMARY KEY,
    username VARCHAR(24) NOT NULL,
    password VARCHAR(124) NOT NULL
)

INSERT INTO users (id, username, password) // вставить в ...
VALUES (4, 'Isa', 'street');
INSERT INTO users (id, username, password)
VALUES (3, 'Ibrashka', 'suuuuyyy');

UPDATE users SET 
password = 'area is a hole', username = 'Ishak'
WHERE id = 4;

DELETE FROM users
WHERE id = 5 or id = ... ;
 
SELECT password FROM users  // SELECT * (for all column)
WHERE id =2 AND id = 3;

ALTER TABLE message 
    ADD COLUMN user_id BIGINT NOT NULL,
    ADD CONSTRAINT user_id_fk  FOREIGN KEY (user_id) 
    REFERENCES users (id);
    
INSERT INTO message (message, user_id)
VALUES ('GBHBDTN ', 2)
INSERT INTO message (message, user_id)
VALUES ('fuhbrfnyfz aeyrwbz cktletobz', 3)

SELECT message.*, users.username FROM message
JOIN users ON users.id = message.user_id;

SELECT SUM(...) FROM users // MAX, MIN
GROUP BY username

SELECT users.*, message.message FROM users
JOIN message ON users.id = message.user_id
GROUP BY username
HAVING id >= 2;"""


// #include <iostream>
// #include <string>
// #include <vector>

// using namespace std;

// void print(string s) {
// //     cout << s << endl;
// //     }

// class Car{
// private:
//     float price;
//     string mark;
    
// public:
//     Car(float price, string mark){
//         this->price = price;
//         this->mark = mark;
//         }
        
//     Car(){}

//     void setValues(float price, string mark){
//         this->price = price;
//         this->mark = mark;
//         }
        
//     void print(){
//         cout << this->price << " - " << this->mark << endl;
//         }
        
// };


// class Motorway : public Car{
    
// };

// int main(){
    
//     Car bmw;
//     bmw.setValues(2300, "i5");
//     bmw.print();
    
//     Car kia;
//     kia.setValues(2100, "k5");
//     kia.print();
    
    
    // print("Python");
    
    // cout << "GBHBDTN" << endl;
    
    // int number = 1;
    // char sym = 'A';
    // bool isGay = false;
    // const float pi = 3.1415;
    // string name = "Den"
    
    // int a, b;
    // cout << "a" << endl;
    // cin >> a;
    // cout << "b" << endl;
    // cin >> b;
    // cout << a+b << endl;
    // cout << a-b << endl;
    // cout << a*b << endl;
    // cout << (float) a/ (float) b << endl;
    // cout << a%b << endl;

    // int h;
    // cin >> h  ;
    // if(h%2 == 0){
    //     cout << "even n" << endl;
    // }else{
    //     cout << "odd number" << endl   ;   
    // }
    
    // int num = 12;
    // switch(num){
    //     case 1:
    //         cout << ... ;
    //         break;
    //     case ...:
    //         cout << ...;
    //         break;
    //     default:
    //         cout<<..;;   
    // }
    
     int iarr[4];
     iarr[0] = 4;
     iarr[4] = 3;
     cout << iarr << endl;
    
     float farr[2] = {1.2, 324.2};
     cout << farr;
    
     for(int i = 100; i >= 5;  i/=2){
         cout<< i << endl;
         }
        
     int i = 9;
     while (i){
         cout << i<< endl;
         i--; 
         }
    
     int val = 9; 
     int *ptr = &val;  // * указатель на переменныую (копируем ссылку)
    
     int &rev = val; // ссылка на перменную   
         return 0;
 }