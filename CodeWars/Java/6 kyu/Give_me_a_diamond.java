class Diamond {
    public static String print(int n) {
         if (n <= 0 || n % 2 == 0) {
            return null; 
        }

        String result = "";

        int middle = n / 2;

        for (int i = 0; i < n; i++) {
            int stars = i <= middle ? 1 + 2 * i : 1 + 2 * (n - i - 1);
            int spaces = (n - stars) / 2;

            
            String line = "";

            for (int s = 0; s < spaces; s++) {
                line += " ";
            }

            for (int a = 0; a < stars; a++) {
                line += "*";
            }
            result += line + "\n";
        }

        return result;
    }
    
}