public String seeColor(String str) {
  if(str.length() >= 3 && str.substring(0, 3).equals("red"))
    return str.substring(0, 3);
  
  if(str.length() >= 4 && str.substring(0, 4).equals("blue"))
    return str.substring(0, 4);
  
  return "";
}
