#include<iostream>
#include<string>
using namespace std;

class Person{
    protected:
    //name, age, gender, contactInfo
    string name;
    int age;
    bool gender;
    string contactInfo;
// Construtor

public :
  Person(string n, int a, bool g, string c){
    name=n;
    age=a;
    gender=g;
    contactInfo=c;

  };

  //setter and Getters

  public: void getName(string na){
     name=na;

    cout<<"The Name :"<<name<<endl;

  };

  public:
   string setName(string na){
    name=na;
   };

   
  public: void getAge(int ag){
    age=ag;
    cout<<"The Age is :"<<age<<endl;

  };

  public:
   int setAge(int ag){
    age=ag;
   };

   
  public: void getGender(bool ge){
    gender=ge;
    cout<<"Gender: "<<gender<<endl;

  };

  public:
   bool setGender(bool ge){
    gender=ge;
   };

  public:
    void  displayInfo(){
        cout<<"Name is: "<<name<<endl;
        cout<<"Age is: "<<age<<endl;
        cout<<"Gender is: "<<gender<<endl;
    
    };
};

    class Doctor:public Person{
        private:
        string specialization;

        public:
         string setSpecialization(string spe){
            specialization=spe;

         };

         public :
          void displayInfo(){
            displayInfo();
            cout<<"Specialization"<<specialization<<endl;
          };





    };




int main(){
    cout<<"Welcome A Nurse Toto Hospital Management System"<<endl;
    cout<<"To Continuee Select  Your Roles :"<<endl;
    cout<<"1.Receptionist"<<endl;
    cout<<"2.Admin"<<endl;
    cout<<"3.Doctor"<<endl;
    cout<<"4.Nurse"<<endl;
    
    int choice =0;
    cout<<"Enter your Choice/Selection";
    cin>>choice;

    if(choice==1){

    }






    return 0;
}