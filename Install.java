class Install{
public static void main(String[] args){

        String a = "C:/Users/Administrator/.jenkins/workspace/test/npp.7.3.1.Installer.exe";
        String b = "C:/Users/Administrator/.jenkins/workspace/test/npp.7.3.*.nstaller.exe";
        if (a < b) {
               Process p = Runtime.getRuntime().exec(filePath1);             
               System.out.println("b is greater than a");
             
        }else {
           Process p = Runtime.getRuntime().exec(filePath);             
           System.out.println("a is less than b");
    }
           
	
}
}
