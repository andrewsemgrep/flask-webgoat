import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Credentials;

public class OkhttpSecretBasicAuth {
  private String username = "wowee";
  private String password = "hi";
  private String empty = "";

  public void run() {
    // ruleid: hardcoded-secret-in-credentials
    String credential = Credentials.basic(username, "asdf");

    // ruleid: hardcoded-secret-in-credentials
    String credential = Credentials.basic(username, password);
    
    // ok: hardcoded-secret-in-credentials
    String credential = Credentials.basic(username, "");

    // ok: hardcoded-secret-in-credentials
    String credential = Credentials.basic(username, empty);

    // ok: hardcoded-secret-in-credentials
    String credential = Credentials.basic(username, System.getenv("PASSWORD"));
  }
}
