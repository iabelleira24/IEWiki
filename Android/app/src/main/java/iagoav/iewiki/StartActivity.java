package iagoav.iewiki;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

public class StartActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);


        SharedPreferences prefs = getSharedPreferences("MyPrefs", MODE_PRIVATE);
        boolean isLoggedIn = prefs.getBoolean("isLoggedIn", false); // TODO: dejar en false false por defecto

        Intent intent;
        if (isLoggedIn) {
            // Si está logueado, ir a MainActivity
            intent = new Intent(this, MainActivity.class);
        } else {
            // Si NO está logueado, ir a LoginActivity
            intent = new Intent(this, LoginActivity.class);

        }



        startActivity(intent);
        finish();
    }
}
