import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.net.InetSocketAddress;

import static java.util.concurrent.Executors.newCachedThreadPool;

class PreviewServer {
    public void run() throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(8000), 0);
        server.createContext("/", new MainPageHandler());
        server.createContext("/preview", new PreviewHandler());
        server.setExecutor(newCachedThreadPool());
        server.start();
    }
}