public class TestComplex {
    public static void main(String[] args) {
    Complex a = new Complex(2.3,4.3);
    Complex b = new Complex(3.14,6.28);
    Complex c = a.add(b);
    System.out.println(c.getReal()+" "+c.getImaginary());
    }
}
class Complex {
    private double real;
    private double imaginary;

    public Complex(double real, double imaginary) {
        this.real = real;
        this.imaginary = imaginary;
    }

    public double getReal() {
        return real;
    }
    public double getImaginary() {
        return imaginary;
    }
     public Complex add(Complex arg){
        double r = this.real + arg.real;
        double i = this.imaginary + arg.imaginary;
        return new Complex(r,i);
     }
    public Complex sup(Complex arg){
        double r = this.real - arg.real;
        double i = this.imaginary - arg.imaginary;
        return new Complex(r,i);
    }
}
