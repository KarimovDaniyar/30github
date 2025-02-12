public class EBook extends  Book{
    double fileSizeMB;
    String fileFormat;

    public EBook(String title, String author, int yearPublished, double price, double fileSizeMB, String fileFormat) {
        super(title, author, yearPublished, price);
        this.fileSizeMB = fileSizeMB;
        this.fileFormat = fileFormat;
    }

    @Override
    String getBookInfo() {
        return super.getBookInfo() + fileSizeMB + fileFormat;
    }

    @Override
    void printBookDetails() {
        bookType();
        super.printBookDetails();
        System.out.println("В формате: "+fileFormat + ", " + fileSizeMB + "MB");
    }

    void bookType(){
        System.out.println("This is an ebook");
    }
}
