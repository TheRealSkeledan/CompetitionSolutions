public String makeOutWord(String out, String word) {
    String first = out.substring(0, 2);
    String last = out.substring(2);

    return first + word + last;
}