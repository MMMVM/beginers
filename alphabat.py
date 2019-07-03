public class test4 {

    public static void main(String[] args) {

        char b = '*';

        if( (b >= 'a' && b <= 'z') || (b >= 'A' && b <= 'Z'))
            System.out.println(b + " is an alphabet.");
        else
            System.out.println(b + " is not an alphabet.");
    }
}
