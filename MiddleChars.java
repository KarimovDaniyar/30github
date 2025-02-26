class MiddleChars {
    public static void main(String[] args) {
        middleChar("abad");
    }
    static void middleChar(String s){
        if (s.length()%2 == 0){
            System.out.println(s.charAt(s.length()/2-1)+","+s.charAt(s.length()/2));
        }else{
            int l = (int)s.length()/2;
            System.out.println(s.charAt(l));
        }
    }
}