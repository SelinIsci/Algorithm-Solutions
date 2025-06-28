public class Kata {
  public static String usdcny(int usd) {
    double rate = 6.75;
    double yuan = rate * usd;
    return String.format("%.2f Chinese Yuan",yuan);
  }
}