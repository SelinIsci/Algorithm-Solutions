import java.util.ArrayList;
import java.util.Arrays;
public class Solution {
  public static int[] distinct(int[] array){
     ArrayList<Integer> uniqueList = new ArrayList<>();

        for (int i = 0; i < array.length; i++) {
            if (!uniqueList.contains(array[i])) {
                uniqueList.add(array[i]);
            }
        }

    
        int[] result = new int[uniqueList.size()];
        for (int i = 0; i < uniqueList.size(); i++) {
            result[i] = uniqueList.get(i);
        }

        return result;
    }
  }