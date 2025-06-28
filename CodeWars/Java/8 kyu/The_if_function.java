public class Kata {
    public static void _if(Boolean bool, Runnable func1, Runnable func2) {
        if (bool != null && bool) {
            if (func1 != null) {
                func1.run();
            }
        } else {
            if (func2 != null) {
                func2.run();
            }
        }
    }
}