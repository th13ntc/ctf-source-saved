import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.net.InetSocketAddress;

class DebugServer {
    public void run() throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(7654), 0);
        server.createContext("/flag", new FlagHandler());
        server.setExecutor(null);
        server.start();
    }
}