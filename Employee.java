abstract class Employee {
    String name;
    int id;
    float baseSalary;

    public Employee(String name, int id, float baseSalary){
        this.name = name;
        this.id = id;
        this.baseSalary = baseSalary;
    }

    abstract float calculateSalary();
    abstract void displayEmployeeInfo();

    public static void main(String[] args) {
        Employee[] employees = new Employee[2];
        employees[0] = new FullTimeEmployee("Daniyar", 0, 8333);
        employees[1] = new ContractEmployee("Idris",1,160,12);
        for(Employee e : employees){
            e.displayEmployeeInfo();
            System.out.println("----------------------");
        }
    }
}

interface Payable{
    float getPaymentAmount();
}

class FullTimeEmployee extends Employee implements Payable{
    static final float benefit = 1.2f;
    boolean healthInsurance = true;

    public FullTimeEmployee(String name, int id, float baseSalary) {
        super(name, id, baseSalary);
    }

    @Override
    float calculateSalary() {
        return baseSalary*benefit;
    }

    @Override
    public float getPaymentAmount(){
        return calculateSalary();
    }

    @Override
    void displayEmployeeInfo() {
        System.out.println("Name: "+name + "\nID: "+id+"\nyour salary is: "+calculateSalary()+"\nHealthy Insurance: "+healthInsurance);
    }
}

class ContractEmployee extends Employee implements Payable{
    float hourlyRate;
    int hourlyWorked;

    public ContractEmployee(String name, int id, int hourlyWorked, float hourlyRate){
        super(name, id, 0);
        this.hourlyRate = hourlyRate;
        this.hourlyWorked = hourlyWorked;
    }

    @Override
    float calculateSalary(){
        return hourlyWorked*hourlyRate;
    }

    @Override
    public float getPaymentAmount(){
        return calculateSalary();
    }

    @Override
    void displayEmployeeInfo(){
        System.out.println("Name: "+name + "\nID: "+id+"\nyour salary is: "+calculateSalary()+"\nHourly Rate: "+hourlyRate);
    }
}