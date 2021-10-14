import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;

import java.io.IOException;
import java.io.OutputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.ThreadLocalRandom;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class PreviewHandler implements HttpHandler {
    static boolean isUrlValid(String url) {
        Pattern domainPattern = Pattern.compile("^https?://[a-z-0-9]+[.][a-z]+.*$", Pattern.CASE_INSENSITIVE);
        Matcher matcher = domainPattern.matcher(url);

        return matcher.find();
    }

    public void handle(HttpExchange httpExchange) throws IOException {
        String url = httpExchange.getRequestURI().getQuery();
        String tmpFilePath = String.format("/tmp/%d.png", Math.abs(ThreadLocalRandom.current().nextInt()));
        byte[] response;

        if (isUrlValid(url)) {
            try {
                String commandArray[] = {
                        "/opt/google/chrome/chrome",
                        "--timeout=30000",
                        "--no-sandbox",
                        "--no-zygote",
                        "--no-service-autorun",
                        "--single-process",
                        "--headless",
                        "--disable-gpu",
                        "--screenshot=" + tmpFilePath,
                        url
                };
                Process process = Runtime.getRuntime().exec(commandArray);

                if (!process.waitFor(30, TimeUnit.SECONDS)) {
                    process.destroy();
                }

                try {
                    response = Files.readAllBytes(Paths.get(tmpFilePath));
                } catch (Exception e) {
                    e.printStackTrace();
                    response = String.format("Failed to read the screenshot for %s", url).getBytes();
                }
            } catch (Exception e) {
                e.printStackTrace();
                response = String.format("Failed to make screenshot for %s", url).getBytes();
            }
        } else {
            response = "URL is invalid".getBytes();
        }

        httpExchange.sendResponseHeaders(200, response.length);
        OutputStream os = httpExchange.getResponseBody();
        os.write(response);
        os.close();

        try {
            Files.delete(Paths.get(tmpFilePath));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}