class Install{
public static void main(String[] args){
	float a = 7.3.1;
	float b = 7.3.*;
        String filepath = "C:/Users/Administrator/.jenkins/workspace/test/npp.7.3.1.Installer.exe";
        String filepath1 = "C:/Users/Administrator/.jenkins/workspace/test/npp.7.3.*.nstaller.exe";
        if (a < b) {
               Process p = Runtime.getRuntime().exec(filepath1);             
               System.out.println("b is greater than a");
             
        }else {
           Process p = Runtime.getRuntime().exec(filepath);             
           System.out.println("a is less than b");
    }
           
	
}
}
