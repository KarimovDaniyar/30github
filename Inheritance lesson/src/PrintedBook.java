public class PrintedBook extends Book{
    int numberOfPages;
    String publisher;

    public PrintedBook(String title, String author, int yearPublished, double price, int numberOfPages, String publisher) {
        super(title, author, yearPublished, price);
        this.numberOfPages = numberOfPages;
        this.publisher = publisher;
    }

    @Override
    String getBookInfo() {
        return super.getBookInfo();
    }

    @Override
    void printBookDetails() {
        bookType();
        super.printBookDetails();
        System.out.println(numberOfPages+"cтр."+" "+ publisher);
    }

    void bookType(){
        System.out.println("This is a printed book");
    }

    void PrintBook(){
        for(int i=0; i < Main.myBooks.length; i++){
            if(Main.myBooks[i] == null){
                Main.myBooks[i] = new PrintedBook(title, author, yearPublished, price, numberOfPages, publisher);
                break;
            }
        }
    }
}
