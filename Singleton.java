class Singleton{
    private static class Instance{
      private static Singleton instance = new Singleton();
    }
  
    private Singleton(){}
    private static Singleton getSingleton(){
        return Instance.instance;
    };

    public static void main(String[] args) {
        
    }
  }