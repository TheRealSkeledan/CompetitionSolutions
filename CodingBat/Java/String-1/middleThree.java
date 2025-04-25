public String middleThree(String str) {
  return str.substring(str.length()/2 - 1, str.length()/2) + str.substring(str.length()/2, str.length()/2 + 1) + str.substring(str.length()/2 + 1, str.length()/2 + 2);
}
