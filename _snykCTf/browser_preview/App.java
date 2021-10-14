public class App {
    public static void main(String[] args) throws Exception {
        (new PreviewServer()).run();
        (new DebugServer()).run();
    }
}
