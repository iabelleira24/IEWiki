package iagoav.iewiki;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

public class LoginActivity extends AppCompatActivity {
    private TextView noTienesC;
    private Context context;
    private RequestQueue queue;
    private EditText usernameL;
    private EditText passwordL;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        context = this;

        noTienesC = findViewById(R.id.btnNoTienesCuenta);
        usernameL = findViewById(R.id.etUsuarioL);
        passwordL = findViewById(R.id.etContrasenaL);
        Button ingresar = findViewById(R.id.btnIngresarL);

        queue = Volley.newRequestQueue(this);

        ingresar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String user = usernameL.getText().toString().trim();
                String pass = passwordL.getText().toString().trim();

                if (user.isEmpty() || pass.isEmpty()) {
                    Toast.makeText(LoginActivity.this, "Completa todos los campos", Toast.LENGTH_SHORT).show();
                    return;
                }

                try {
                    JSONObject obj = new JSONObject();
                    obj.put("username", user);
                    obj.put("password", pass);

                    JsonObjectRequest request = new JsonObjectRequest(
                            Request.Method.POST,
                            "http://10.0.2.2:8000/login/",
                            obj,
                            new Response.Listener<JSONObject>() {
                                @Override
                                public void onResponse(JSONObject response) {
                                    try {
                                        String token = response.getString("token");
                                        SharedPreferences prefs = getSharedPreferences("app", MODE_PRIVATE);
                                        prefs.edit().putString("token", token).apply();

                                        Intent intent = new Intent(context, MainActivity.class);
                                        startActivity(intent);
                                        finish();
                                    } catch (JSONException e) {
                                        e.printStackTrace();
                                        Toast.makeText(LoginActivity.this, "Error al procesar respuesta", Toast.LENGTH_SHORT).show();
                                    }
                                }
                            },
                            new Response.ErrorListener() {
                                @Override
                                public void onErrorResponse(VolleyError error) {
                                    if (error.networkResponse != null) {
                                        int statusCode = error.networkResponse.statusCode;
                                        if (statusCode == 404) {
                                            Toast.makeText(LoginActivity.this, "Usuario no encontrado", Toast.LENGTH_SHORT).show();
                                        } else if (statusCode == 403) {
                                            Toast.makeText(LoginActivity.this, "Contraseña incorrecta", Toast.LENGTH_SHORT).show();
                                        }
                                    } else {
                                        Toast.makeText(LoginActivity.this, "Error de conexión", Toast.LENGTH_SHORT).show();
                                    }
                                }
                            }
                    );

                    queue.add(request);
                } catch (JSONException e) {
                    e.printStackTrace();
                    Toast.makeText(LoginActivity.this, "Error al crear solicitud", Toast.LENGTH_SHORT).show();
                }
            }
        });

        noTienesC.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(context, RegisterActivity.class);
                startActivity(intent);
            }
        });
    }
}
