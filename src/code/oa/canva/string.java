package code.oa.canva;
public class string {
    public static int hash(String s) {
        int hash = 0;

        for (int i = 0;i < s.length(); i++) {
            hash += (i % 2) * (i + 1) * (s.charAt(i) - 'a' + 1);
            // System.out.println((i % 2) * (i + 1) * (s.charAt(i) - 'a' + 1));
        }

        return hash;
    }

    public static void main(String[] args) {
        System.out.println(hash("abeaa"));
        System.out.println();

        System.out.println(hash("veoylywz"));
        System.out.println(hash("qtmzmzwu"));
        System.out.println();
        System.out.println(hash("vogxnwpy"));
        System.out.println(hash("ofjrdyiy"));
        System.out.println();
        System.out.println(hash("avzzcwqq"));
        System.out.println(hash("sitrntdy"));
        System.out.println();
        System.out.println(hash("wrsxmvdx"));
        System.out.println(hash("quwydsry"));
        System.out.println();


    }


}
