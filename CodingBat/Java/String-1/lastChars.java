public String lastChars(String a, String b) {
    a = a.length() <= 0 ? "@" : a;
    b = b.length() <= 0 ? "@" : b;

    return a.substring(0, 1) + b.substring(b.length() - 1);
}
